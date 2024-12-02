# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 2,  # Replace with actual sample answer for part 1
            2: 4   # Replace with actual sample answer for part 2
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
        #return [int(line) for line in input_str.split('\n')]
        return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    def check_list_is_valid(report):
        isAscending = True
        isDesending = True
        isAdjacent = True

        for i in range(len(report)-1):
                if report[i] >= report[i+1]:
                    isAscending = False
                if report[i] <= report[i+1]:
                    isDesending = False
                if abs(report[i]-report[i+1]) > 3:
                    isAdjacent = False
        if (isDesending or isAscending) and isAdjacent:
            return True
        
        return False

    def solve_part1(self, data: Any) -> Union[int, str]:
        safe_cnt = 0

        for report in data:
            if AoCSolver.check_list_is_valid(report):
                safe_cnt += 1

        return safe_cnt

    def solve_part2(self, data: Any) -> Union[int, str]:
        safe_cnt = 0
        
        for report in data:
            if AoCSolver.check_list_is_valid(report):
                safe_cnt += 1
                continue
            
            #If not a safe List try to bumb one value and check again    
            for skipId in range(len(report)):

                temp_list = [report[i] for i in range(len(report)) if i != skipId]
                
                if AoCSolver.check_list_is_valid(temp_list):
                    print(f"{report}: Wird sicher nach Entfernen von {report[skipId]} -> {temp_list}")
                    safe_cnt += 1
                    break

        return safe_cnt


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
    
    # Test with sample input
    sample_input = solver.read_file("sample.txt")
    sample_answer = solver.solve(sample_input)
    expected = solver.sample_answers[solver.level]
    
    print(f"Sample answer: {sample_answer}")
    assert sample_answer == expected, f"Expected {expected}, got {sample_answer}"
    
    # Solve actual input
    input_data = solver.read_file("input.txt")
    answer = solver.solve(input_data)
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()