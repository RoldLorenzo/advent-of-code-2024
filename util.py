import sys

# https://adventofcode.com/2024

def get_filename() -> str:
    if len(sys.argv) <= 1:
        print("Usage: <script.py> <input file name>")
        sys.exit(1)
        
    return sys.argv[1]

def file_as_string() -> str:
    with open(get_filename(), 'r') as input:
        return input.read()

def file_lines() -> list[str]:
    with open(get_filename(), 'r') as input:
        return [line.rstrip('\n') for line in input]

def print_results(part_one, part_two):
    print("---Part One:---")
    print(part_one)
    print()
    print("---Part Two:---")
    print(part_two)