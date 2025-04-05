from util import *
from typing import Optional

directions = [
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]

def get_word(input: list[str], i: int, j: int, i_offset: int, j_offset: int, length: int) -> str:    
    word = ""
    for _ in range(length):
        c = get_matrix_element(input, i, j)
        if c is None: break
        
        word += c
        i += i_offset
        j += j_offset
        
    return word

def count_xmases(input: list[str]) -> int:
    total = 0
    
    for i, string in enumerate(input):
        for j, char in enumerate(string):
            if char != "X": continue
            
            words = [get_word(input, i, j, dir[0], dir[1], 4) for dir in directions]
            total += sum(1 for word in words if word == "XMAS")
                
    return total

def count_x_mases(input: list[str]) -> int:
    total = 0
    
    for i, string in enumerate(input):
        for j, char in enumerate(string):
            if char != "A": continue
            
            positive_diagonal = get_word(input, i - 1, j - 1, 1, 1, 3)
            negative_diagonal = get_word(input, i + 1, j - 1, -1, 1, 3)
            targets = {"MAS", "SAM"}
            if positive_diagonal in targets and negative_diagonal in targets:
                total += 1
                
    return total

if __name__ == "__main__":
    input = file_lines()
    
    part_one = count_xmases(input)
    part_two = count_x_mases(input)
    
    print_results(part_one, part_two)