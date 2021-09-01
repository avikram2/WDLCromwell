
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--operand1', type=int)
    parser.add_argument('--operand2', type=int)
    args = parser.parse_args()
    sum = args.operand1 + args.operand2
    print(sum)