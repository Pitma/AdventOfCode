# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 161,  # Replace with actual sample answer for part 1
            2: 48   # Replace with actual sample answer for part 2
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
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    def solve_part1(self, data: Any) -> Union[int, str]:
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
        matches = re.finditer(pattern, data)
        
        number_pairs = [(int(match.group(1)) * int(match.group(2))) 
                    for match in matches]
        
        return sum(number_pairs)

    def find_smaller_value(array, target):
        smaller_nums = [x for x in array if x < target]
        if smaller_nums:
            return max(smaller_nums)
        return None

    def solve_part2(self, data: Any) -> Union[int, str]:
        muls = [(m.start(), m.group(1), m.group(2)) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', data)]

        dos = [m.start() for m in re.finditer(r'\w*do\(\)', data)]

        donts = [m.start() for m in re.finditer(r'(\w*don\'t)\(\)', data)]

        
        valid_pairs = []

        for mul_pos, num1, num2 in muls:

            do = AoCSolver.find_smaller_value(dos,mul_pos)
            dont = AoCSolver.find_smaller_value(donts,mul_pos)
            
            if dont is None or (do is not None and do >= dont):
                valid_pairs.append((int(num1)* int(num2)))
                
        return sum(valid_pairs)

    def solve(self, input_str: str) -> Union[int, str]:
        """Main solve method."""
        data = self.parse_input(input_str)
        return self.solve_part1(data) if self.level == 1 else self.solve_part2(data)

    @staticmethod
    def read_file(filename: str) -> str:
        """Read input file."""
        return Path(filename).read_text().strip()

def main():
    solver = AoCSolver(level=2)  # Change level as needed
    
    # Test with sample input
    sample_input = solver.read_file("sample.txt")
    sample_answer = solver.solve(sample_input)
    expected = solver.sample_answers[solver.level]
    
    print(f"Sample answer: {sample_answer}")
    assert sample_answer == expected, f"Expected {expected}, got {sample_answer}"
    
    # Solve actual input
    input_data = solver.read_file("input.txt")
    answer = solver.solve(input_data)
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()