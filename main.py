import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(description="Run an Advent of Code Solution.")
    parser.add_argument(
        "--day", type=int, required=True, help="Day number (e.g., 1 for day01)"
    )
    parser.add_argument(
        "--part", type=int, default=1, choices=[1, 2], help="Part number (1 or 2)"
    )
    args = parser.parse_args()

    # Format day folder with zero padding if needed (e.g., day01, day02, etc.)
    day_module = importlib.import_module(f"2015.day{args.day:02d}.solution")

    # Read the corresponding input file.
    input_path = f"2023/day{args.day:02d}/input.txt"
    with open(input_path) as f:
        input_data = f.read()

    data = day_module.parse_input(input_data)

    if args.part == 1:
        result = day_module.part1(data)
    else:
        result = day_module.part2(data)

    print(f"Day {args.day:02d} - Part {args.part}: {result}")


if __name__ == "__main__":
    main()
