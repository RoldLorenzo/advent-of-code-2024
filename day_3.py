from util import *

class InstructParser:
    def __init__(self, input: str):
        self.input = input
        self.position = 0
        self.active = True

    def parse(self) -> tuple[int, int]:
        part_one = 0
        part_two = 0
        
        while not self.is_at_end():
            if self.match("mul"):
                result = self.parse_mul()
                
                part_one += result
                
                if self.active: 
                    part_two += result
            elif self.match("don't"):
                self.set_active(False)
            elif self.match("do"):
                self.set_active(True)
            else:
                self.advance()
        
        return (part_one, part_two)
    
    # With 'mul' already consumed, expect '(<number>,<number>)' and return the 2 number multiplied.
    # If the arguments are not correctly formated, or if self.active is false, return 0.  
    def parse_mul(self) -> int:        
        if not self.match("("):
            return 0
        
        num1 = self.parse_number()
        
        if not self.match(","):
            return 0
        
        num2 = self.parse_number()
        
        if not self.match(")"):
            return 0

        return num1 * num2
    
    # With 'do' or 'don't' already consumed, expect '()'.
    # If '()' gets consumed, set self.active to value.
    def set_active(self, value: bool):
        if self.match("()"):
            self.active = value
    
    def parse_number(self):
        number_txt = ""
        while not self.is_at_end() and self.peek(1).isdecimal(): 
            number_txt += self.advance()
            
        return int(number_txt)
    
    def advance(self):
        self.position += 1
        return self.input[self.position - 1]
    
     # Consumes the next chars if they are equal to expected
    def match(self, expected: str) -> bool:
        if self.is_at_end() or self.peek(len(expected)) != expected:
            return False
        
        self.position += len(expected)
        return True
    
    # Returns the next n chars without consuming them
    def peek(self, n: int) -> str:
        if self.is_at_end(): 
            return ""
        
        return self.input[self.position : self.position + n]

    def is_at_end(self) -> bool:
        return self.position >= len(self.input)

if __name__ == "__main__":
    input = file_as_string()
    
    parser = InstructParser(input)
    part_one, part_two = parser.parse()
    
    print_results(part_one, part_two)