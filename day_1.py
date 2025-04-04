from util import *
from collections import Counter

if __name__ == "__main__":
    pairs = [line.split() for line in file_lines()]
    
    first_list = sorted(map(lambda p: int(p[0]), pairs))
    second_list = sorted(map(lambda p: int(p[1]), pairs))
    
    part_one = sum(abs(f - s) for f, s in zip(first_list, second_list))    
    
    second_counter = Counter(second_list)
    part_two = sum(x * second_counter[x] for x in first_list)

    print_results(part_one, part_two)