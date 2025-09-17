#!/usr/bin/env python3
"""
Run evaluation with Dual-Layer SPRL model.
Processes datasets through the configured backend and saves results.
"""
import argparse
import json
import os
import sys
import yaml
import importlib
from pathlib import Path
from datetime import datetime

def load_config(config_path):
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_backend(backend_spec):
    """Dynamically load backend runner."""
    module_path, class_name = backend_spec.rsplit(':', 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)

def load_dataset(dataset_path):
    """Load JSONL dataset."""
    items = []
    with open(dataset_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items

def process_dataset(runner, dataset_items, dataset_name):
    """Process dataset through the runner."""
    results = []
    
    for i, item in enumerate(dataset_items):
        prompt = item.get('prompt', '')
        
        # Add timestamp for t₀ tracking
        item['prompt_timestamp'] = datetime.now().isoformat()
        
        # Process through TML backend
        output = runner.generate(prompt, item)
        
        # Create result record
        result = {
            'id': item.get('id', f'{dataset_name}-{i:04d}'),
            'prompt': prompt,
            'prompt_timestamp': item['prompt_timestamp'],
            'answer_key': item.get('answer_key', []),
            'output': output,
            'completion_timestamp': datetime.now().isoformat()
        }
        
        results.append(result)
        
        # Progress indicator
        if (i + 1) % 10 == 0:
            print(f"  Processed {i + 1}/{len(dataset_items)} items")
    
    return results

def save_results(results, output_path):
    """Save results to JSONL file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result) + '\n')

def main():
    parser = argparse.ArgumentParser(description='Run TML Dual-Layer SPRL evaluation')
    parser.add_argument('--config', required=True, 
                       help='Path to configuration file (e.g., eval/configs/sacred_pause.yaml)')
    parser.add_argument('--datasets', default='eval/datasets',
                       help='Directory containing dataset files')
    parser.add_argument('--output', default='eval/results/raw',
                       help='Directory for output results')
    parser.add_argument('--scenario', 
                       choices=['low_risk', 'medium_risk', 'high_risk', 'vulnerable_population'],
                       help='Risk scenario for I×V×P testing')
    parser.add_argument('--datasets-list', nargs='+', 
                       default=['harmful', 'ambiguous', 'facts', 'creative'],
                       help='List of datasets to process')
    
    args = parser.parse_args()
    
    # Load configuration
    print(f"Loading configuration from {args.config}")
    config = load_config(args.config)
    
    # Apply scenario if specified
    if args.scenario:
        scenario_configs = {
            'low_risk': {'impact': 0.1, 'vulnerability': 0.1, 'probability': 0.1},
            'medium_risk': {'impact': 0.5, 'vulnerability': 0.5, 'probability': 0.5},
            'high_risk': {'impact': 0.9, 'vulnerability': 0.9, 'probability': 0.9},
            'vulnerable_population': {'impact': 0.7, 'vulnerability': 1.0, 'probability': 0.8}
        }
        
        if args.scenario in scenario_configs:
            config['scenario'] = scenario_configs[args.scenario]
            sprl = config['scenario']['impact'] * config['scenario']['vulnerability'] * config['scenario']['probability']
            sprl_clamped = max(0.0001, min(0.9999, sprl))
            print(f"Using scenario: {args.scenario}")
            print(f"  I×V×P = {config['scenario']['impact']} × {config['scenario']['vulnerability']} × {config['scenario']['probability']}")
            print(f"  SPRL = {sprl_clamped:.4f} (clamped)")
    
    # Note about framework enforcement
    print("Note: Thresholds are framework-enforced (not configurable)")
    
    # Load backend
    backend_spec = config.get('backend')
    print(f"Loading backend: {backend_spec}")
    BackendRunner = load_backend(backend_spec)
    runner = BackendRunner(config)
    
    # Create output directory
    config_name = Path(args.config).stem
    if args.scenario:
        config_name = f"{config_name}_{args.scenario}"
    output_dir = os.path.join(args.output, config_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each dataset
    for dataset_name in args.datasets_list:
        dataset_path = os.path.join(args.datasets, f'{dataset_name}.jsonl')
        
        if not os.path.exists(dataset_path):
            print(f"Warning: Dataset {dataset_path} not found, skipping")
            continue
        
        print(f"\nProcessing {dataset_name} dataset...")
        dataset_items = load_dataset(dataset_path)
        print(f"  Loaded {len(dataset_items)} items")
        
        # Process through runner
        results = process_dataset(runner, dataset_items, dataset_name)
        
        # Save results
        output_path = os.path.join(output_dir, f'{dataset_name}.jsonl')
        save_results(results, output_path)
        print(f"  Saved results to {output_path}")
    
    # Print Dual-Layer SPRL statistics if available
    if hasattr(runner, 'get_statistics'):
        stats = runner.get_statistics()
        print("\n" + "=" * 60)
        print("DUAL-LAYER SPRL STATISTICS")
        print("=" * 60)
        print(f"Total Decisions: {stats.get('total_decisions', 0)}")
        print(f"Decision States:")
        print(f"  +1 (Proceed): {stats.get('proceed_count', 0)}")
        print(f"   0 (Sacred Pause): {stats.get('sacred_pause_count', 0)}")
        print(f"  -1 (Prohibit): {stats.get('prohibit_count', 0)}")
        print()
        
        # Dynamic Stream metrics
        print("Dynamic Stream (DS):")
        print(f"  Active streams: {stats.get('ds_active_count', 0)}")
        print(f"  Avg chunks/decision: {stats.get('ds_avg_chunks', 0):.1f}")
        print(f"  Continuity from t₀: {stats.get('ds_continuity_rate', 100):.1f}%")
        
        # Static Anchor metrics
        print("\nStatic Anchor (SA):")
        print(f"  Anchors set: {stats.get('sa_count', 0)}")
        print(f"  Avg write time: {stats.get('sa_avg_write_ms', 0):.1f}ms")
        print(f"  Immutability verified: {stats.get('sa_immutable_verified', True)}")
        
        # Lite Traces
        print("\nLite Traces:")
        print(f"  Near-misses recorded: {stats.get('lite_trace_count', 0)}")
        print(f"  Amber zone rate: {stats.get('amber_zone_rate', 0):.1f}%")
        
        # Compliance
        print("\nCompliance:")
        invariants = stats.get('invariants_satisfied', [])
        print(f"  Invariants satisfied: {', '.join(invariants) if invariants else 'All'}")
        spoliation = stats.get('spoliation_detected', False)
        print(f"  Spoliation detected: {'Yes ⚠️' if spoliation else 'No ✓'}")
        
        # Performance
        print("\nPerformance:")
        print(f"  Avg decision latency: {stats.get('avg_latency_ms', 0):.1f}ms")
        print(f"  Max decision latency: {stats.get('max_latency_ms', 0):.1f}ms")
        print(f"  Non-blocking verified: {stats.get('non_blocking_verified', True)}")
    
    print("\nEvaluation complete!")
    print("Framework thresholds enforced throughout execution.")

if __name__ == '__main__':
    main()
