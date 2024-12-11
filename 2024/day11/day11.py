# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 55312,  # Replace with actual sample answer for part 1
            2: 65601038650482   # Replace with actual sample answer for part 2
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
        return [line for line in input_str.split(' ')]
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str
    @staticmethod
    def apply_rules(input):

        new_stones = []
        for stone in input:
            if stone == '0': 
                new_stones.append('1') 
                continue
            if len(stone) % 2 == 0: 
                new_stones.append(str(int(stone[:len(stone)//2])))
                new_stones.append(str(int(stone[len(stone)//2:])))
                continue
            new_stones.append(str(int(stone) * 2024))
        
        return new_stones
    
    @staticmethod
    def apply_rules_fast(input,set_blinks):

        blinks = 0
        stone_types = {}
        for i_stone in input:
            stone_types[i_stone] = stone_types.get(i_stone, 0) + 1
        print("start", stone_types)
        while blinks != set_blinks:
            new_stones = {}
            for stone,cnt in stone_types.items():
                if stone == '0':
                    new_stones['1'] = new_stones.get('1',0) + cnt
                    continue
                if len(stone) % 2 == 0: 
                    left = stone[:len(stone)//2]
                    right = stone[len(stone)//2:]
                    new_stones[str(int(left))] = new_stones.get(str(int(left)),0) + cnt
                    new_stones[str(int(right))] = new_stones.get(str(int(right)),0) + cnt
                    continue
                new_stones[str(int(stone)*2024)] = new_stones.get(str(int(stone)*2024),0) + cnt
                
            stone_types = new_stones.copy() 
            blinks +=1
        return stone_types

            
    def solve_part1(self, data: Any) -> Union[int, str]:
        blinks = 0
        stones = data
        while blinks != 75:
            stones = self.apply_rules(stones)
            blinks += 1

        return len(stones)
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        return sum(self.apply_rules_fast(data,75).values())
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