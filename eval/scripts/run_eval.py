#!/usr/bin/env python3
"""
Run evaluation with post-audit TML model.
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
        
        # Process through TML backend
        output = runner.generate(prompt, item)
        
        # Create result record
        result = {
            'id': item.get('id', f'{dataset_name}-{i:04d}'),
            'prompt': prompt,
            'answer_key': item.get('answer_key', []),
            'output': output,
            'timestamp': datetime.now().isoformat()
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
    parser = argparse.ArgumentParser(description='Run TML evaluation')
    parser.add_argument('--config', required=True, 
                       help='Path to configuration file (e.g., eval/configs/sacred_pause.yaml)')
    parser.add_argument('--datasets', default='eval/datasets',
                       help='Directory containing dataset files')
    parser.add_argument('--output', default='eval/results/raw',
                       help='Directory for output results')
    parser.add_argument('--override', action='append', default=[],
                       help='Override config values (e.g., --override config.sprl_threshold=0.3)')
    parser.add_argument('--datasets-list', nargs='+', 
                       default=['harmful', 'ambiguous', 'facts', 'creative'],
                       help='List of datasets to process')
    
    args = parser.parse_args()
    
    # Load configuration
    print(f"Loading configuration from {args.config}")
    config = load_config(args.config)
    
    # Apply overrides
    for override in args.override:
        key_path, value = override.split('=')
        keys = key_path.split('.')
        
        # Navigate to the nested key
        current = config
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        # Set the value (try to parse as float/int/bool)
        try:
            current[keys[-1]] = float(value)
        except ValueError:
            if value.lower() == 'true':
                current[keys[-1]] = True
            elif value.lower() == 'false':
                current[keys[-1]] = False
            else:
                current[keys[-1]] = value
    
    # Load backend
    backend_spec = config.get('backend')
    print(f"Loading backend: {backend_spec}")
    BackendRunner = load_backend(backend_spec)
    runner = BackendRunner(config)
    
    # Create output directory
    config_name = Path(args.config).stem
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
    
    # Print TML statistics if available
    if hasattr(runner, 'get_statistics'):
        stats = runner.get_statistics()
        print("\n" + "=" * 60)
        print("TML Framework Statistics")
        print("=" * 60)
        print(f"Total Decisions: {stats['total_decisions']}")
        print(f"Sacred Pause Triggers: {stats['sacred_pause_triggers']}")
        print(f"Trigger Rate: {stats['trigger_rate']:.1f}%")
        print(f"SPRL Threshold: {stats['threshold']}")
        print()
        
        # Calibration guidance
        if stats['trigger_rate'] < 1:
            print("⚠ Very low trigger rate - consider lowering threshold")
        elif stats['trigger_rate'] > 50:
            print("⚠ Very high trigger rate - consider raising threshold")
        else:
            print("✓ Trigger rate appears balanced")
    
    print("\nEvaluation complete!")

if __name__ == '__main__':
    main()
