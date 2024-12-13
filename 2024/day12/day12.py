# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 1930,  # Replace with actual sample answer for part 1
            2: 80   # Replace with actual sample answer for part 2
        }
        
        # Common direction vectors
        self.directions = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1)
            # 'NE': (-1, 1),
            # 'SE': (1, 1),
            # 'SW': (1, -1),
            # 'NW': (-1, -1)
        }

    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        # return [line for line in input_str.split('\n')]
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        return [[[c , False] for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def is_valid_position(x: int, y: int, grid) -> bool:
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        rows = len(data)
        cols = len(data[0])
        #print(data)
        regions = {}
        group = 0

        def check_neighbors(r,c):

            data[r][c][1] = True

            for d , (dx,dy) in self.directions.items():
                    new_r, new_c = r + 1 * dx, c + 1 * dy
                    
                    if not self.is_valid_position(new_r,new_c,data): 
                        regions.setdefault(group,{'plots':0,'fences':0})['fences'] += 1 
                        continue
                    check_value, check_visited = data[new_r][new_c]
                    if check_value != value: 
                        regions.setdefault(group,{'plots':0,'fences':0})['fences'] += 1 
                        continue
                    if not check_visited:
                        regions.setdefault(group,{'plots':0,'fences':0})['plots'] += 1 
                        check_neighbors(new_r,new_c)

        
        for r in range(rows):
            for c in range(cols):
                value , visited = data[r][c] 
                if visited == True: continue
                group += 1
                regions.setdefault(group,{'plots':0,'fences':0})['plots'] += 1 
                check_neighbors(r,c)
                
        costs = sum(region['plots']* region['fences'] for key, region in regions.items())
        return costs

        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
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