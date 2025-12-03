# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 357,  # Replace with actual sample answer for part 1
            2: 3121910778619   # Replace with actual sample answer for part 2
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
        return [[int(c) for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        #print(data)
        sum = 0

        for cur_set in data:  
            first_position = []
            searching = True

            #print(f"Searching in set: {set}")
            for i in range(9, 0, -1):
                for j, val in enumerate(cur_set):
                    if val == i:
                        first_position.append([i,j])
                        #print(f"Found {i} at position {j}")
            first_position.sort(key=lambda x: x[1])
            max_combi = 0

            for i in range(len(first_position)):
                value_i,index_i = first_position[i]   
                for j in range(i+1, len(first_position)):
                    value_j,index_j = first_position[j]
                    if index_j > index_i:
                        candidate_str = str(value_i) + str(value_j)
                        candidate_num = int(candidate_str)
            
                        if candidate_num > max_combi:
                            max_combi = candidate_num

            #print(f"Best Combination:",max_combi)
            sum += max_combi
        return sum
                             
            
        raise NotImplementedError("Part 1 solution not implemented")

    def find_highest_between(self, first_position, start_index, end_index):
        max_value = 0
        for value, index in first_position:
            if start_index <= index <= end_index:
                if value > max_value:
                    max_value = value
        return max_value
    
    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        sum = 0

        for cur_set in data:  
            first_position = []

            #print(f"Searching in set: {cur_set}")
            for i in range(9, 0, -1):
                for j, val in enumerate(cur_set):
                    if val == i:
                        first_position.append([i,j])
                        #print(f"Found {i} at position {j}")
            first_position.sort(key=lambda x: x[1])
            #print(first_position)
            max_combi = ""

            start = 0
            for i in range(12,0,-1):
                highest = self.find_highest_between(first_position, start, len(cur_set)-i)
                #print(f"Highest between {start} and {len(cur_set)-i} is {highest}")
                max_combi += str(highest)
                       
                for value, index in first_position:
                    if value == highest and index >= start and index <= len(cur_set)-i:
                        start = index + 1
                        break
            #print(f"Current combination: {max_combi}")
            sum += int(max_combi)
        return sum
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