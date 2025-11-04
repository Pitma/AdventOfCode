# template.py
from collections import defaultdict, deque, Counter
from itertools import permutations
import numpy as np
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 0,  # Replace with actual sample answer for part 1
            2: 0   # Replace with actual sample answer for part 2
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
        #return [line for line in input_str.split('\n')]
        return [int(line) for line in input_str.split('\n')]
        #return [list(map(int, re.findall(r'(\d+)', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        print(data) 
        max_sum = 150
        count = 0
        n = len(data)
        for i in range(1 << n):
            s = 0
            for j in range(n):
                if (i & (1 << j)) > 0:
                    s += data[j]
            if s == max_sum:
                count += 1
        return count     
       

        raise NotImplementedError("Part 1 solution is not implemented yet")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        print(data) 
        max_sum = 150
        count = 0
        n = len(data)
        size_counts = {}
        for i in range(1 << n):
            s = 0
            num_containers = 0
            for j in range(n):
                if (i & (1 << j)) > 0:
                    s += data[j]
                    num_containers += 1
            if s == max_sum:
                count += 1
                size_counts[num_containers] = size_counts.get(num_containers, 0) + 1
        if size_counts:
            print("Minimum containers:", size_counts[min(size_counts.keys())])
        #return count     
        return 0 
        raise NotImplementedError("Part 2 solution is not implemented yet")

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