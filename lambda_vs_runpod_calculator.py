#!/usr/bin/env python3
"""
Lambda Labs vs RunPod H100 SXM5 Cost Benchmark Calculator 2026.
Compares on-demand spot and reserved rates for 8x H100 GPU clusters.
"""
import argparse

def benchmark_h100(hours, lambda_rate, runpod_rate):
    lambda_total = hours * lambda_rate
    runpod_total = hours * runpod_rate
    diff = lambda_total - runpod_total
    annual_diff = diff * (8760.0 / hours) if hours > 0 else 0.0
    return {
        "lambda_total": lambda_total,
        "runpod_total": runpod_total,
        "diff": diff,
        "annual_diff": annual_diff
    }

def main():
    parser = argparse.ArgumentParser(description="Lambda Labs vs RunPod H100 Cost Benchmark")
    parser.add_argument("--hours", type=float, default=500.0, help="Training duration in hours (default: 500)")
    parser.add_argument("--lambda-rate", type=float, default=3.29, help="Lambda Labs H100 hourly rate (default: $3.29)")
    parser.add_argument("--runpod-rate", type=float, default=2.89, help="RunPod H100 SXM hourly rate (default: $2.89)")
    args = parser.parse_args()

    res = benchmark_h100(args.hours, args.lambda_rate, args.runpod_rate)
    print(f"Workload Duration:       {args.hours:.0f} hours")
    print(f"Lambda Labs (@${args.lambda_rate:.2f}/hr): ${res['lambda_total']:.2f}")
    print(f"RunPod (@${args.runpod_rate:.2f}/hr):      ${res['runpod_total']:.2f}")
    print(f"Training Run Savings:    ${res['diff']:.2f}")

if __name__ == "__main__":
    main()
