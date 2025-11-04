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
            1: 4,  # Replace with actual sample answer for part 1
            2: 7   # Replace with actual sample answer for part 2
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
        #return [int(line) for line in input_str.split('\n')]
        #return [list(map(int, re.findall(r'(\d+)', line))) for line in input_str.split('\n')]
        return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    def check_neighbors(self, grid, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == '#':
                    count += 1
        return count
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        #print(data)
        for step in range(100):
            new_grid = [row.copy() for row in data]
            for i in range(len(data)):
                for j in range(len(data[0])):
                    neighbors = self.check_neighbors(data, i, j)
                    if data[i][j] == '#':
                        if neighbors not in [2, 3]:
                            new_grid[i][j] = '.'
                    else:
                        if neighbors == 3:
                            new_grid[i][j] = '#'
            data = new_grid
        self.print_grid(data)
        lights = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == '#':
                    lights += 1
        return lights
        raise NotImplementedError("Part 1 solution is not implemented yet")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        #print(data)
        data[0][0] = '#'
        data[0][len(data[0])-1] = '#'
        data[len(data)-1][0] = '#'
        data[len(data)-1][len(data[0])-1] = '#'
        for step in range(100):
            new_grid = [row.copy() for row in data]
            for i in range(len(data)):
                for j in range(len(data[0])):
                    neighbors = self.check_neighbors(data, i, j)
                    if data[i][j] == '#':
                        if neighbors not in [2, 3]:
                            new_grid[i][j] = '.'
                    else:
                        if neighbors == 3:
                            new_grid[i][j] = '#'
            
            new_grid[0][0] = '#'
            new_grid[0][len(data[0])-1] = '#'
            new_grid[len(data)-1][0] = '#'
            new_grid[len(data)-1][len(data[0])-1] = '#'
            data = new_grid
        self.print_grid(data)
        lights = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == '#':
                    lights += 1
        return lights
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