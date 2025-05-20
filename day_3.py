from util import *
import re

def parse_only_muls(input: str) -> int:
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    result = 0
    
    for match in re.finditer(pattern, input):
        result += int(match.group(1)) * int(match.group(2))
            
    return result

def parse_instructions(input: str) -> int:
    active = True
    result = 0
    pattern = r"""
        mul\((?P<x>-?\d+),(?P<y>-?\d+)\) |
        (?P<do>do\(\)) |
        (?P<dont>don't\(\))
    """
    
    for match in re.finditer(pattern, input, flags=re.VERBOSE):        
        if match.group("do"):
            active = True  
            continue
              
        if match.group("dont"):
            active = False
            continue
        
        x = match.group("x")
        y = match.group("y")
        if active:
            result += int(x) * int(y)
            
    return result

if __name__ == "__main__":
    input = file_as_string()
    
    part_one = parse_only_muls(input)
    part_two = parse_instructions(input)
    
    print_results(part_one, part_two)