import argparse
from .wrapper import DummyModel, generate_with_sprl
from .risk_engine import RiskEngine

def main():
    parser = argparse.ArgumentParser("sprl-demo")
    parser.add_argument("prompt", help="input text (quoted)")
    parser.add_argument("--threshold", type=float, default=0.6, help="anchor threshold (0..1)")
    parser.add_argument("--near-miss", type=float, default=0.3, help="near-miss lower bound")
    args = parser.parse_args()

    model = DummyModel()
    sprl = RiskEngine(threshold=args.threshold, near_miss_floor=args.near_miss)
    out = generate_with_sprl(args.prompt, model, sprl)
    print(out)

if __name__ == "__main__":
    main()
