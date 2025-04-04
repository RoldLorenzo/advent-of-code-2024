from util import *

class InstructParser:
    def __init__(self, input: str):
        self.input = input
        self.position = 0
        self.active = True

    def parse_only_mul(self) -> int:
        total = 0
        while not self.is_at_end():
            if self.match("mul"):
                total += self.parse_mul()
            else:
                self.advance()
        
        return total

    def parse(self) -> int:
        total = 0
        while not self.is_at_end():
            if self.match("mul"):
                total += self.parse_mul()
            elif self.match("don't"):
                self.set_active(False)
            elif self.match("do"):
                self.set_active(True)
            else:
                self.advance()
        
        return total
                
    def parse_mul(self) -> int:
        if not self.active:
            return 0
        
        if not self.match("("):
            return 0
        
        num1 = self.parse_number()
        
        if not self.match(","):
            return 0
        
        num2 = self.parse_number()
        
        if not self.match(")"):
            return 0

        return num1 * num2
    
    def set_active(self, value: bool):
        if not self.match("()"):
            return
        
        self.active = value
    
    def parse_number(self):
        number_txt = ""
        while not self.is_at_end() and self.peek(1).isdecimal(): 
            number_txt += self.advance()
            
        return int(number_txt)
    
    def advance(self):
        self.position += 1
        return self.input[self.position - 1]
            
    def match(self, esperado: str) -> bool:
        if self.is_at_end() or self.peek(len(esperado)) != esperado:
            return False
        
        self.position += len(esperado)
        return True
        
    def peek(self, n: int) -> str:
        if self.is_at_end(): return ""
        return self.input[self.position : self.position + n]

    def is_at_end(self) -> bool:
        return self.position >= len(self.input)

if __name__ == "__main__":
    input = file_as_string()
    
    parser = InstructParser(input)
    part_one = parser.parse_only_mul()
    
    parser = InstructParser(input)
    part_two = parser.parse()
    
    print_results(part_one, part_two)