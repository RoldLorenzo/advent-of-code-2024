from util import *
from typing import Any

type Rules = dict[str, set[str]]

def swap(lst: list[Any], i: int, j: int):
    lst[i], lst[j] = lst[j], lst[i]

# Create a dict that relates each number to the set of numbers that must come after it.
# Example:
# ['75|47', '75|36', '47|23'] -> {'75': {'47', '36'}, '47': {'23'}}
def create_rules_dict(rules: list[str]) -> Rules:
    rule_dict: Rules = {}
    
    for line in rules:
        a, b = line.split("|")
        rule_dict.setdefault(a, set()).add(b)
        
    return rule_dict

def page_follows_rules(page: list[str], rules: Rules) -> bool:
    for i, a in enumerate(page):
        for b in page[i:]:
            if b in rules and a in rules[b]: 
                return False
            
    return True

def reorder_page(page: list[str], rules: Rules):
    for i in range(len(page)):       
        while True:
            swapped = False
            
            for j in range(i, len(page)):
                if page[j] in rules and page[i] in rules[page[j]]:
                    swap(page, i, j)
                    swapped = True
                    break
            
            if not swapped: break
                
def reorder_incorrect_pages(pages: list[list[str]], rules: Rules) -> list[list[str]]:
    incorrect_pages = [page for page in pages if not page_follows_rules(page, rules)]
    
    for page in incorrect_pages:
        reorder_page(page, rules)
    
    return incorrect_pages
       
if __name__ == "__main__":
    [rules_str, pages_str] = file_as_string().split("\n\n")
    rules = create_rules_dict(rules_str.strip().splitlines())
    pages = [page.split(",") for page in pages_str.strip().splitlines()]
   
    part_one = sum(int(page[len(page) // 2]) for page in pages if page_follows_rules(page, rules))

    fixed_pages = reorder_incorrect_pages(pages, rules)
    part_two = sum(int(page[len(page) // 2]) for page in fixed_pages)
    
    print_results(part_one, part_two)