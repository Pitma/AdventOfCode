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
            1: 62842880,  # Replace with actual sample answer for part 1
            2: 57600000   # Replace with actual sample answer for part 2
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
        return [line for line in input_str.split('\n')]
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    def calculate_ingredient_by_share(self, ingredients, shares):
        total = [0, 0, 0, 0]
        for i in range(len(ingredients)):
            for j in range(4):
                total[j] += int(ingredients[i][j]) * int(shares[i])
        for j in range(4):
            if total[j] < 0:
                total[j] = 0
        score = total[0] * total[1] * total[2] * total[3]
        return score
    
    def calculate_ingredient_calories_by_share(self, ingredients, shares):
        total = [0, 0, 0, 0,0]
        for i in range(len(ingredients)):
            for j in range(5):
                total[j] += int(ingredients[i][j]) * int(shares[i])
        for j in range(4):
            if total[j] < 0:
                total[j] = 0
        score = total[0] * total[1] * total[2] * total[3]
        calories = total[4]
        if calories != 500:
            return 0
        return score
    
    def simplex_raster(self,step=10):
        kombis = []
        werte = range(0, 101, step) 
        for a in werte:
            for b in werte:
                for c in werte:
                    d = 100 - (a + b + c)
                    if 0 <= d <= 100:
                        kombis.append([a, b, c, d])
        return kombis
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        print(data) 
        ingedients = []
        for line in data:
            #  capacity -1, durability -2, flavor 6, texture 3, calories 8
            matches = re.match(r'.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', line)
            if matches:
                ingedients.append([matches.group(1),matches.group(2),matches.group(3),matches.group(4)]) 

        for i in range(len(ingedients)):
            for j in range(4):
                ingedients[i][j] = int(ingedients[i][j])
        shares = self.simplex_raster(step=1)
        max_score = 0
        for shares in shares:
            score = self.calculate_ingredient_by_share(ingedients, shares)
            if score > max_score:
                max_score = score
        return max_score
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        print(data) 
        ingedients = []
        for line in data:
            #  capacity -1, durability -2, flavor 6, texture 3, calories 8
            matches = re.match(r'.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', line)
            if matches:
                ingedients.append([matches.group(1),matches.group(2),matches.group(3),matches.group(4),matches.group(5)]) 

        for i in range(len(ingedients)):
            for j in range(5):
                ingedients[i][j] = int(ingedients[i][j])
        shares = self.simplex_raster(step=1)
        max_score = 0
        for shares in shares:
            score = self.calculate_ingredient_calories_by_share(ingedients, shares)
            if score > max_score:
                max_score = score
        return max_score
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