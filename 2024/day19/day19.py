# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
from time import time
from functools import cache
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 6,  # Replace with actual sample answer for part 1
            2: 16   # Replace with actual sample answer for part 2
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
        return input_str.split('\n\n')
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    def solve_part1(self, data: Any) -> Union[int, str]:
        allowed_groups = set([group.strip() for group in data[0].split(',')])
        sorted_groups = sorted(allowed_groups, key=len, reverse=True)
        words_to_check = data[1].split('\n')
        max_len = max(map(len,allowed_groups))

        @cache
        def validate_word(word):
            if word == "":
                return True 
            for i in range(max_len+1):
                if word[:i] in sorted_groups and validate_word(word[i:]):
                    return True
            return False
        
        result = 0
        for word in words_to_check:
            result += validate_word(word)
            
        return result

        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        allowed_groups = set([group.strip() for group in data[0].split(',')])
        sorted_groups = sorted(allowed_groups, key=len, reverse=True)
        words_to_check = data[1].split('\n')
        max_len = max(map(len,allowed_groups))

        @cache
        def validate_word(word):
            if word == "":
                return True 
            cnt = 0
            for i in range(min(len(word),max_len)+1):
                if word[:i] in sorted_groups:
                    cnt += validate_word(word[i:])
            return cnt
        
        result = 0
        for word in words_to_check:
            result += validate_word(word)
            
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