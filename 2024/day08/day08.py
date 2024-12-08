# template.py
from collections import defaultdict, deque, Counter
import itertools
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 14,  # Replace with actual sample answer for part 1
            2: 34   # Replace with actual sample answer for part 2
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
    def is_valid_position(x: int, y: int, grid) -> bool:
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def find_influenced_fields(self,key,combos,grid,locations):
        
        for combo in combos:
            p1x, p2x, p1y, p2y, dx, dy = self.get_path(combo)

            n1x,n1y = p1x + (dx * -1), p1y + (dy * -1)
            if AoCSolver.is_valid_position(n1x,n1y,grid):
                locations.add((n1x,n1y))

            n2x,n2y = p2x + dx, p2y + dy
            if AoCSolver.is_valid_position(n2x,n2y,grid):
                locations.add((n2x,n2y))

    def get_path(self, combo):
        p1x,p2x,p1y,p2y = combo[0][0],combo[1][0],combo[0][1],combo[1][1]
        dx,dy = p2x-p1x, p2y-p1y
        
        return p1x,p2x,p1y,p2y,dx,dy

    def find_influenced_fields_recur(self,key,combos,grid,locations):
        
        for combo in combos:
            p1x,p2x,p1y,p2y,dx,dy = self.get_path(combo) 

            n1x,n1y = p1x + (dx * -1), p1y + (dy * -1)
            while True:
            
                if AoCSolver.is_valid_position(n1x,n1y,grid):
                    locations.add((n1x,n1y))
                    n1x += dx * -1
                    n1y += dy * -1
                else: break

            n2x,n2y = p2x + dx, p2y + dy
            while True:
                if AoCSolver.is_valid_position(n2x,n2y,grid):
                    locations.add((n2x,n2y))
                    n2x += dx
                    n2y += dy
                else: break
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        locations = set()
        rows = len(data)
        cols = len(data[0])
        found_antennas = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if data[i][j] != '.':
                    found_antennas[data[i][j]].append([i,j])
        for antenna_key,positions in found_antennas.items():
            combinations = list(itertools.combinations(positions, 2))

            self.find_influenced_fields(antenna_key,combinations,data,locations)

        return len(locations)
        raise NotImplementedError("Part 1 solution not implemented")


    def solve_part2(self, data: Any) -> Union[int, str]:
        locations = set()
        rows = len(data)
        cols = len(data[0])
        found_antennas = defaultdict(list)
        result = 0
        for i in range(rows):
            for j in range(cols):
                if data[i][j] != '.':
                    found_antennas[data[i][j]].append([i,j])
                    locations.add((i,j))
        for antenna_key,positions in found_antennas.items():
            combinations = list(itertools.combinations(positions, 2))

            self.find_influenced_fields_recur(antenna_key,combinations,data,locations)

        return len(locations)
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