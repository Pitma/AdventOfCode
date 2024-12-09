# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 1928,  # Replace with actual sample answer for part 1
            2: 2858   # Replace with actual sample answer for part 2
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
        return [int(line) for line in input_str]
        #return  [for c in line in input_str.split())
        return input_str

    def solve_part1(self, data: Any) -> Union[int, str]:
        
        def check_integers_after(arr, start_index):
            for i in range(start_index, len(arr)):
                if isinstance(arr[i], int):
                    return True
            return False
        
        id_counter = 0
        iblocks = []
        datablock = True
        for block in data:
            if datablock:
                iblocks.extend([id_counter]*block)
                id_counter += 1
            else:
                iblocks.extend('.'*block)
            datablock = not datablock

        dots = []
        blocks = []
        for idx,space in enumerate(iblocks):
            if space == '.':
                dots.append(idx)
            else:
                blocks.append(idx)

        blocks = sorted(blocks,reverse=True)
        dots = sorted(dots)
        
        for idx, d in enumerate(dots): 
            if not check_integers_after(iblocks,d):
                break

            iblocks[d], iblocks[blocks[0]] =  iblocks[blocks[0]],iblocks[d]
            blocks.pop(0)

        sum = 0
        for idx, block in enumerate(iblocks):
            if block == '.':
                break            
            sum += idx * block    

        return sum
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        
        def shift_blocks(arr):
            result = arr.copy()
            blocks = []
            i = 0
            while i < len(result):
                if result[i] != '.':
                    num = result[i]
                    length = 0
                    while i + length < len(result) and result[i + length] == num:
                        length += 1
                    blocks.append((int(num), length, i))
                    i += length
                else:
                    i += 1
                    
            blocks.sort(reverse=True)
            
            for num, length, old_pos in blocks:
                new_pos = -1
                for i in range(old_pos): 
                    if all(result[j] == '.' for j in range(i, i + length)):
                        new_pos = i
                        break
                        
                if new_pos != -1:
                    for i in range(old_pos, old_pos + length):
                        result[i] = '.'
                        
                    for i in range(length):
                        result[new_pos + i] = int(num)
                        
            return result
        
        
        id_counter = 0
        iblocks = []
        datablock = True
        for block in data:
            if datablock:
                iblocks.extend([id_counter]*block)
                id_counter += 1
            else:
                iblocks.extend('.'*block)
            datablock = not datablock

        new_iblocks = shift_blocks(iblocks)

        sum = 0
        for idx, block in enumerate(new_iblocks):
            if block == '.':
                continue           
            sum += idx * block    

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