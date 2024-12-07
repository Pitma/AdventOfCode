# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
from itertools import product
import re
import operator

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 3749,  # Replace with actual sample answer for part 1
            2: 11387   # Replace with actual sample answer for part 2
        }
        
        # Common direction vectors
        self.directions = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1),
            'NE': (-1, 1),
            'SE': (1, 1),
            'SW': (1, -1),
            'NW': (-1, -1)
        }

        
    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        # return [line for line in input_str.split('\n')]
        #return [int(line) for line in input_str.split('\n')]
        return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    def solve_part1(self, data: Any) -> Union[int, str]:
        ops = {
            '+': operator.iadd,
            '*': operator.imul,
        }

        res = 0
        for calc in data:
            target = calc[0]  
            numbers = calc[1:] 
            op_len = len(numbers) - 1
            combinations = product(["+","*"], repeat=op_len)
            comb_result = [''.join(combo) for combo in combinations]
            print("Target:", target, "Zahlen:", numbers)

            for op in comb_result:
                result = numbers[0]  
                
                for i in range(len(op)):
                    next_num = numbers[i + 1]
                    result = ops[op[i]](result, next_num)

                    
                if result == target:
                    res += result
                    break

        return res    
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        ops = {
            '+': operator.iadd,
            '*': operator.imul
        }

        res = 0
        for calc in data:
            target = calc[0]  
            numbers = calc[1:] 
            op_len = len(numbers) - 1
            combinations = product(["+","*","|"], repeat=op_len)
            comb_result = [''.join(combo) for combo in combinations]
            print("Target:", target, "Zahlen:", numbers)

            for op in comb_result:

                result = numbers[0]  
                
                for i in range(len(op)):
                    next_num = numbers[i + 1]
                    if op[i] != "|":
                        result = ops[op[i]](result, next_num)
                    else:
                        result = int(f"{result}{next_num}")
                if result == target:
                    res += result
                    break

        return res    
        raise NotImplementedError("Part 2 solution not implemented")

    def solve(self, input_str: str) -> Union[int, str]:
        """Main solve method."""
        data = self.parse_input(input_str)
        return self.solve_part1(data) if self.level == 1 else self.solve_part2(data)

    @staticmethod
    def read_file(filename: str) -> str:
        """Read input file."""
        return Path(filename).read_text().strip()

def main():
    solver = AoCSolver(level=1)  # Change level
    
    # Test
    sample_input = solver.read_file("sample.txt")
    sample_answer = solver.solve(sample_input)
    expected = solver.sample_answers[solver.level]
    
    print(f"Sample answer: {sample_answer}")
    assert sample_answer == expected, f"Expected {expected}, got {sample_answer}"
    
    # Solve
    input_data = solver.read_file("input.txt")
    answer = solver.solve(input_data)
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()