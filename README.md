# Advent of Code 2015 Solutions

This repository contains my solutions to the Advent of Code 2015
challenges. Each day's puzzle is implemented in its own directory under
the `2015` folder, with input files, solution scripts, and tests.

## Project Structure
advent_of_code/
├── 2023/
│   ├── day01/
│   │   ├── __init__.py
│   │   ├── solution.py      # Contains functions for part1() and part2()
│   │   ├── input.txt        # Your puzzle input
│   │   └── test_day01.py    # Optional: unit tests for your solutions
│   ├── day02/
│   │   ├── __init__.py
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── test_day02.py
│   └── ... (and so on for each day)
├── common/
│   ├── __init__.py
│   └── utils.py           # Common helper functions, parsers, etc.
└── main.py                # Optional: a runner script to execute any day’s solution

