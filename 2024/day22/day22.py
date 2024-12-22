# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re
import numpy as np

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 37327623,  # Replace with actual sample answer for part 1
            2: 23   # Replace with actual sample answer for part 2
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
        return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    def solve_part1(self, data: Any) -> Union[int, str]:

        def calculate(num):
            num = (num ^ (num * 64)) % 16777216
            if num == 100000000: num = 16113920
            num = (num ^ (num // 32)) % 16777216
            if num == 100000000: num = 16113920
            num = (num ^ (num * 2048)) % 16777216
            if num == 100000000: num = 16113920
            return num
        
        sum = 0
        for d in data:
            num = d
            for i in range(2000):
                num = calculate(num)
            sum += num
        return sum
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
            
        def calculate(num):
            num = (num ^ (num * 64)) % 16777216
            if num == 100000000: num = 16113920
            num = (num ^ (num // 32)) % 16777216
            if num == 100000000: num = 16113920
            num = (num ^ (num * 2048)) % 16777216
            if num == 100000000: num = 16113920
            return num
        
        buyers = []
        seq_total = {}
        for line in data:
            num = line
            buyer = [num % 10]
            for _ in range(2000):
                num = calculate(num)
                buyer.append(num % 10)
            seen = set()
            for i in range(len(buyer)-4):
                a,b,c,d,e = buyer[i:i+5]
                seq = (b-a,c-b,d-c,e-d)
                if seq in seen: continue
                seen.add(seq)
                if seq not in seq_total: 
                    seq_total[seq] = 0
                seq_total[seq] += e
            
            buyers.append(buyer)
        return max(seq_total.values())

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
    solver = AoCSolver(level=2)  # Change level
    
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