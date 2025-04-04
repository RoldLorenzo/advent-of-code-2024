from util import *
from itertools import pairwise, combinations
import operator

def differences_in_interval(report: list[int], min: int, max: int) -> bool:
    return all(min <= abs(a - b) <= max for a, b in pairwise(report))

def all_increasing_or_decreasing(report: list[int]) -> bool:
    if len(report) < 2: 
        return True
    
    compare = operator.lt if report[0] < report[1] else operator.gt
    
    return all(compare(a, b) for a, b in pairwise(report))

def is_safe(report: list[int]) -> bool:
    return all_increasing_or_decreasing(report) and differences_in_interval(report, 1, 3)

# Returns True if the report is safe, or if removing
# exactly one of its elements makes it safe;
# Returns False otherwise.
def some_combination_safe(report: list[int]) -> bool:
    return (
        is_safe(report) or
        any(is_safe(list(c)) for c in combinations(report, len(report) - 1))
    )

if __name__ == "__main__":
    reports = list(map(lambda line: list(map(int, line.split())), file_lines()))
    
    part_one = sum(1 for report in reports if is_safe(report))
    part_two = sum(1 for report in reports if some_combination_safe(report))
    
    print_results(part_one, part_two)