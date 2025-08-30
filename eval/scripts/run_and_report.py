#!/usr/bin/env python3
"""
Run complete evaluation pipeline and generate comprehensive report.
Compares baseline vs Sacred Pause with different thresholds.
"""
import argparse
import subprocess
import os
import sys
from datetime import datetime

def run_configuration(config_path, threshold=None, output_dir='eval/results/raw'):
    """Run evaluation for a specific configuration."""
    cmd = ['python', 'eval/scripts/run_eval.py', '--config', config_path, '--output', output_dir]
    
    if threshold is not None:
        cmd.extend(['--override', f'config.sprl_threshold={threshold}'])
    
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error running configuration: {result.stderr}")
        return False
    
    print(result.stdout)
    return True

def main():
    parser = argparse.ArgumentParser(
        description='Run complete TML evaluation pipeline with multiple configurations'
    )
    parser.add_argument('--output', default='eval/results/raw',
                       help='Output directory for results')
    parser.add_argument('--thresholds', nargs='+', type=float,
                       default=[0.3, 0.5, 0.7, 0.9],
                       help='SPRL thresholds to test')
    parser.add_argument('--skip-baseline', action='store_true',
                       help='Skip baseline evaluation')
    parser.add_argument('--report-only', action='store_true',
                       help='Only generate report from existing results')
    
    args = parser.parse_args()
    
    if not args.report_only:
        print("=" * 80)
        print("TML EVALUATION PIPELINE - POST-AUDIT MODEL")
        print("=" * 80)
        print(f"Started at: {datetime.now().isoformat()}")
        print(f"Output directory: {args.output}")
        print(f"Thresholds to test: {args.thresholds}")
        print()
        
        # Run baseline (no TML)
        if not args.skip_baseline:
            print("\n" + "=" * 60)
            print("RUNNING BASELINE (No TML)")
            print("=" * 60)
            success = run_configuration('eval/configs/baseline.yaml', output_dir=args.output)
            if not success:
                print("Baseline evaluation failed")
                sys.exit(1)
        
        # Run Sacred Pause with different thresholds
        for threshold in args.thresholds:
            print("\n" + "=" * 60)
            print(f"RUNNING SACRED PAUSE (Threshold = {threshold})")
            print("=" * 60)
            
            # Create unique output directory for each threshold
            threshold_output = os.path.join(args.output, f'sacred_pause_t{int(threshold*100):03d}')
            
            # Run with modified threshold
            cmd = [
                'python', 'eval/scripts/run_eval.py',
                '--config', 'eval/configs/sacred_pause.yaml',
                '--output', args.output,
                '--override', f'config.sprl_threshold={threshold}'
            ]
            
            # Modify the output directory name to include threshold
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"Sacred Pause evaluation failed for threshold {threshold}")
                print(result.stderr)
                continue
            
            print(result.stdout)
    
    # Generate comprehensive report
    print("\n" + "=" * 80)
    print("GENERATING COMPREHENSIVE REPORT")
    print("=" * 80)
    
    # Run scoring scripts
    cmd = ['python', 'eval/scripts/score_all.py', '--raw', args.output, '--verbose']
    subprocess.run(cmd)
    
    # Generate comparison report
    print("\n" + "=" * 80)
    print("THRESHOLD COMPARISON ANALYSIS")
    print("=" * 80)
    
    configs = os.listdir(args.output)
    sacred_pause_configs = [c for c in configs if c.startswith('sacred_pause')]
    
    if sacred_pause_configs:
        print("\nComparing Sacred Pause configurations:")
        print("-" * 40)
        
        # Extract threshold from config name and sort
        threshold_data = []
        for config in sacred_pause_configs:
            # Try to extract threshold from config name
            if config == 'sacred_pause':
                threshold_data.append((0.5, config))  # Default
            else:
                # Extract from name like sacred_pause_t030
                try:
                    t_value = int(config.split('_t')[-1]) / 100.0
                    threshold_data.append((t_value, config))
                except:
                    threshold_data.append((0.5, config))
        
        threshold_data.sort()
        
        print(f"{'Threshold':<12} {'Trigger Rate':<15} {'Recommendation'}")
        print("-" * 50)
        
        for threshold, config in threshold_data:
            # Calculate trigger rate (simplified - would need actual data)
            print(f"{threshold:<12.1f} {'[See above]':<15} ", end='')
            
            if threshold < 0.4:
                print("Low threshold - high logging")
            elif threshold < 0.7:
                print("Balanced threshold")
            else:
                print("High threshold - minimal logging")
    
    # Final recommendations
    print("\n" + "=" * 80)
    print("EVALUATION COMPLETE")
    print("=" * 80)
    print(f"Completed at: {datetime.now().isoformat()}")
    print()
    print("KEY INSIGHTS:")
    print("1. Lower thresholds (0.3-0.4) provide comprehensive logging but higher storage")
    print("2. Medium thresholds (0.5-0.6) balance accountability and efficiency")
    print("3. Higher thresholds (0.7-0.9) minimize logging but may miss important decisions")
    print()
    print("REMEMBER: Organizations must determine appropriate thresholds for their domain.")
    print("These evaluations demonstrate the framework, not prescribe settings.")
    print()
    print("Contact Information:")
    print("- Email: leogouk@gmail.com")
    print("- Successor Contact: support@tml-goukassian.org")
    print("- See Succession Charter: /TML-SUCCESSION-CHARTER.md")

if __name__ == '__main__':
    main()
