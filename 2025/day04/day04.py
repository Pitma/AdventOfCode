# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 13,  # Replace with actual sample answer for part 1
            2: 43   # Replace with actual sample answer for part 2
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
        return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)
    
    def count_neighbors(self, grid, row, col, target):
        count = 0
        for dr, dc in self.directions.values():
            r, c = row + dr, col + dc     
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == target:
                    count += 1
        return count

    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        self.print_grid(data)
        result = 0
        for c in range(len(data)):
            for r in range(len(data[0])):
                if data[r][c] != '@':
                    continue
                if self.count_neighbors(data, r, c, '@') < 4:
                    result += 1
        return result    
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        #self.print_grid(data)
        result = 0
        new_grid = [row[:] for row in data]
        searching = True
        
        while searching:
            hits = 0
            tmp_grid = [row[:] for row in new_grid]
            for c in range(len(new_grid)):
                for r in range(len(new_grid[0])):
                    if new_grid[r][c] != '@':
                        continue
                    if self.count_neighbors(new_grid, r, c, '@') < 4:
                        tmp_grid[r][c] = '.'
                        result += 1
                        hits += 1
            if hits == 0:
                searching = False
            new_grid = [row[:] for row in tmp_grid]
        #self.print_grid(new_grid)   
        return result
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