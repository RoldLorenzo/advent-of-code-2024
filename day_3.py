from util import *
import re

def parse_only_muls(input: str) -> int:
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    result = 0
    
    for match in re.finditer(pattern, input):
        n1 = match.group(1)
        n2 = match.group(2)
        if n1 and n2:
            result += int(n1) * int(n2)
            
    return result

def parse_instructions(input: str) -> int:
    active = True
    result = 0
    pattern = r"""
        mul\((-?\d+),(-?\d+)\)|
        do\(\)|
        don't\(\)
    """
    
    for match in re.finditer(pattern, input, flags=re.VERBOSE):
        full_match = match.group(0)
        
        if full_match == "do()":
            active = True
            continue
        
        if full_match == "don't()":
            active = False
            continue
        
        group_1 = match.group(1)
        group_2 = match.group(2)
        if group_1 and group_2 and active:
            result += int(group_1) * int(group_2)
            
    return result

if __name__ == "__main__":
    input = file_as_string()
    
    part_one = parse_only_muls(input)
    part_two = parse_instructions(input)
    
    print_results(part_one, part_two)