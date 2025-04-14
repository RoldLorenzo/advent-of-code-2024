import sys
import os
from typing import Optional

# https://adventofcode.com/2024

def get_filename() -> str:
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        day_number = os.path.basename(sys.argv[0]).removeprefix("day_").removesuffix(".py")
        input_file = f"input{day_number}.txt"

    if not os.path.exists(input_file):
        print("I was unable to find an input file")
        sys.exit(1)
    
    return input_file

def file_as_string() -> str:
    with open(get_filename(), 'r') as input:
        return input.read().strip()

def file_lines() -> list[str]:
    with open(get_filename(), 'r') as input:
        return input.read().strip().splitlines()

def get_matrix_element(matrix: list[str], i: int, j: int) -> Optional[str]:
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        return matrix[i][j]
    
    return None

def print_results(part_one, part_two):
    print("---Part One:---")
    print(part_one)
    print()
    print("---Part Two:---")
    print(part_two)