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
        #return [list(map(int, re.findall(r'(\d):.(\w+):.(\d+),.(\w+):.(\d+),.(\w+):.(\d+)', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        #print(data) 
        sue_list = []
        for line in data:
            #print(line)
            matches = re.match(r'.*?(\d+):.(\w+):.(\d+),.(\w+):.(\d+),.(\w+):.(\d+)', line)
            sue_list.append([matches.group(1),matches.group(2),matches.group(3),matches.group(4),matches.group(5),matches.group(6),matches.group(7)]) 
        
        #print(sue_list)
        sues = {}
        for match in sue_list:
            #print(match)
            sue_id = int(match[0])
            properties = {match[1]: int(match[2]),
                          match[3]: int(match[4]),
                          match[5]: int(match[6])}
            sues[sue_id] = properties
        
        known_properties = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }
        for sue_id in list(sues.keys()):
            sue_properties = sues[sue_id]
            for prop, val in sue_properties.items():
                if prop in known_properties and known_properties[prop] != val:
                    del sues[sue_id]
                    break
        
        for i in sues:
            print('Sue no. ',i, sues[i])

        raise NotImplementedError("Part 1 solution is implemented but no return value provided")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        sue_list = []
        for line in data:
            #print(line)
            matches = re.match(r'.*?(\d+):.(\w+):.(\d+),.(\w+):.(\d+),.(\w+):.(\d+)', line)
            sue_list.append([matches.group(1),matches.group(2),matches.group(3),matches.group(4),matches.group(5),matches.group(6),matches.group(7)]) 
        
        #print(sue_list)
        sues = {}
        for match in sue_list:
            #print(match)
            sue_id = int(match[0])
            properties = {match[1]: int(match[2]),
                          match[3]: int(match[4]),
                          match[5]: int(match[6])}
            sues[sue_id] = properties
        
        known_properties = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }
        for sue_id in list(sues.keys()):
            sue_properties = sues[sue_id]
            for prop, val in sue_properties.items():
                if prop in known_properties:
                    if prop in ['cats', 'trees']:
                        if val <= known_properties[prop]:
                            del sues[sue_id]
                            break
                    elif prop in ['pomeranians', 'goldfish']:
                        if val >= known_properties[prop]:
                            del sues[sue_id]
                            break
                    else:
                        if known_properties[prop] != val:
                            del sues[sue_id]
                            break
        
        for i in sues:
            print('Sue no. ',i, sues[i])

        raise NotImplementedError("Part 2 solution is implemented but no return value provided")

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