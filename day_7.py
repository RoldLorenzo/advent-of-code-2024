from util import *
from itertools import product
import operator
from dataclasses import dataclass
from typing import Callable

@dataclass
class Equation:
    expected_result: int
    terms: list[int]

type Operator = Callable[[int, int], int]

def concat_int(a: int, b: int) -> int:
    return int(str(a) + str(b))

def evaluate(equation: Equation, operators: list[Operator]) -> int:
    result = equation.terms[0]
    
    for i, op in enumerate(operators):
        result = op(result, equation.terms[i + 1])
    
    return result

def equation_is_possible(equation: Equation, using: list[Operator]) -> bool:    
    for operators in product(using, repeat = len(equation.terms) - 1):
        result = evaluate(equation, operators)
        
        if result == equation.expected_result:
            return True
        
    return False

def sum_possible_equations(equations: list[Equation], using: list[Operator]) -> int:
    return sum(equation.expected_result for equation in equations if equation_is_possible(equation, using))

def str_to_equation(txt: str) -> Equation:
    equation_txt = txt.split(":", 1)
    
    expected_result = int(equation_txt[0])
    terms = [int(num) for num in equation_txt[1].split()]

    return Equation(expected_result, terms)

if __name__ == "__main__":
    equations = [str_to_equation(line) for line in file_lines()]
    
    part_one = sum_possible_equations(equations, [operator.add, operator.mul])
    part_two = sum_possible_equations(equations, [operator.add, operator.mul, concat_int])
    
    print_results(part_one, part_two)