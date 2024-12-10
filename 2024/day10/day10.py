# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 36,  # Replace with actual sample answer for part 1
            2: 81   # Replace with actual sample answer for part 2
        }
        
        # Common direction vectors
        self.directions = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1),
        }
        self.hits = 0
    @staticmethod
    def is_valid_position(x: int, y: int, grid) -> bool:
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        # return [line for line in input_str.split('\n')]
        #return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        return [[int(c) for c in line] for line in input_str.split('\n')]
        return input_str

    def solve_part1(self, data: Any) -> Union[int, str]:
        rows = len(data)
        cols = len(data[0])
        paths = []
        def find_next_step(r,c):
            for d,(dx,dy) in self.directions.items():
                next_r,next_c = r + 1 * dx, c + 1 * dy
                if not AoCSolver.is_valid_position(next_r,next_c,data):
                    continue
                if not data[next_r][next_c] == data[r][c] + 1:
                    continue
                if data[next_r][next_c] == 9 and (next_r,next_c) not in heads_hit:
                    heads_hit.add((next_r,next_c))
                    continue
                
                find_next_step(next_r,next_c)

        for c in range(cols):
            for r in range(rows):
                if data[r][c] == 0:
                    heads_hit = set()
                    find_next_step(r,c)
                    paths.append(len(heads_hit))
        
        return(sum(paths))

        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        rows = len(data)
        cols = len(data[0])
        paths = []
        def find_next_step(r,c):
            for d,(dx,dy) in self.directions.items():
                next_r,next_c = r + 1 * dx, c + 1 * dy
                if not AoCSolver.is_valid_position(next_r,next_c,data):
                    continue
                if not data[next_r][next_c] == data[r][c] + 1:
                    continue
                if data[next_r][next_c] == 9:
                    self.hits +=1
                    continue
                
                find_next_step(next_r,next_c)

        for c in range(cols):
            for r in range(rows):
                if data[r][c] == 0:
                    find_next_step(r,c)
                    paths.append(self.hits)
                    self.hits = 0
        
        return(sum(paths))
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