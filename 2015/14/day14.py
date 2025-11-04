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
            1: 2660,  # Replace with actual sample answer for part 1
            2: 1564   # Replace with actual sample answer for part 2
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

    
    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        print(data) 
        deer_list = []
        for line in data:
            matches = re.match(r'^(\w+).*?(\d+).*?(\d+).*?(\d+)', line)
            if matches:
                deer_list.append([matches.group(1),matches.group(2),matches.group(3),matches.group(4)])
        max_distance = 0
        max_seconds = 2503
        print(deer_list)
        for deer in deer_list:
            speed = int(deer[1])
            fly_time = int(deer[2])
            rest_time = int(deer[3])
            cycle_time = fly_time + rest_time
            full_cycles = max_seconds // cycle_time
            remaining_time = max_seconds % cycle_time
            distance = full_cycles * speed * fly_time
            if remaining_time >= fly_time:
                distance += speed * fly_time
            else:
                distance += speed * remaining_time
            if distance > max_distance:
                max_distance = distance

        return max_distance
    
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        deer_list = []
        for line in data:
            matches = re.match(r'^(\w+).*?(\d+).*?(\d+).*?(\d+)', line)
            if matches:
                deer_list.append([matches.group(1),matches.group(2),matches.group(3),matches.group(4),0,0,0,0])  # Last element for points
        max_distance = 0
        max_seconds = 2503
        print(deer_list)
        for time in range(max_seconds):
            for deer in deer_list:
                name = deer[0]
                speed = int(deer[1])
                fly_time = int(deer[2])
                rest_time = int(deer[3])
                break_time = int(deer[4])
                remaining_flytime = int(deer[5])
                current_distance = int(deer[6])
                if break_time == 0:
                    current_distance += speed
                    remaining_flytime += 1
                    if remaining_flytime == fly_time:
                        break_time = rest_time
                        remaining_flytime = 0
                else:
                    break_time -= 1
   
                deer[4] = break_time
                deer[5] = remaining_flytime
                deer[6] = current_distance

                if current_distance > max_distance:
                    max_distance = current_distance
            
            for deer in deer_list:
                if int(deer[6]) == max_distance:
                    deer[7] += 1  

        max_points = 0
        for deer in deer_list:
            if deer[7] > max_points:
                max_points = deer[7]
            print(deer)

        return max_points
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