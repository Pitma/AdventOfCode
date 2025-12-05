# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 3,  # Replace with actual sample answer for part 1
            2: 14   # Replace with actual sample answer for part 2
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
        return [line for line in input_str.split('\n\n')]
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
        fresh_list = [list(line.split('-')) for line in data[0].split('\n')]
        ingredients = [int(line) for line in data[1].split('\n')]
        cnt = 0
        for ingredient in ingredients:
            for fresh in fresh_list:
                low, high = int(fresh[0]), int(fresh[1])
                if low <= ingredient <= high:
                    cnt += 1
                    break
        return cnt
        raise NotImplementedError("Part 1 solution not implemented")
    def clean_ranges(self, ranges):
        
        merged_ranges = []
        current_low, current_high = ranges[0][0], ranges[0][1]

        for next_low, next_high in ranges[1:]:
            if next_low <= current_high + 1:
                current_high = max(current_high, next_high)
            else:
                merged_ranges.append([current_low, current_high])
                current_low, current_high = next_low, next_high

        merged_ranges.append([current_low, current_high])

        #print("merged:", merged_ranges)
        return merged_ranges

    def solve_part2(self, data: Any) -> Union[int, str]:
        #print(data)
        fresh_list = [list(map(int,(line.split('-')))) for line in data[0].split('\n')]
        fresh_list.sort(key=lambda x: x[0])
        #print(fresh_list)
        cnt = 0
        fresh_list.sort(key=lambda x: x[0])
        total_list = self.clean_ranges(fresh_list)
        for fresh in total_list:
            low, high = fresh[0], fresh[1]
            cnt += (high - low + 1)
        return cnt
        # if cnt not in [14740028503927]:
        #     return cnt
        # else:
        #     return 999
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