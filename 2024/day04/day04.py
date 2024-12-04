# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 18,  # Replace with actual sample answer for part 1
            2: 9   # Replace with actual sample answer for part 2
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

        self.xdirections = {
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
    
    
    def find_xmas_patterns(self, grid, pattern, direction_list):
        rows = len(grid)
        cols = len(grid[0])
        found_patterns = []

        def is_valid_position(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def check_pattern(start_x, start_y, dx, dy):

            current_pattern = []
            
            for i in range(len(pattern)):
                curr_x = start_x + i * dx
                curr_y = start_y + i * dy
                
                if not is_valid_position(curr_x, curr_y):
                    return None
                if grid[curr_x][curr_y] != pattern[i]:
                    return None
                    
                current_pattern.append((curr_x, curr_y))
            
            return current_pattern

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == pattern[0]:
                    for direction, (dx, dy) in direction_list.items():
                        pattern_found = check_pattern(i, j, dx, dy)
                        if pattern_found:
                            found_patterns.append({
                                'start': (i, j),
                                'direction': direction,
                                'path': pattern_found
                            })

        return found_patterns
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        #print(data)
        results = self.find_xmas_patterns(data,"XMAS", self.directions)

        print(f"Gefundene Muster: {len(results)}")
        return len(results)
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        results = self.find_xmas_patterns(data,"MAS", self.xdirections)

        print(f"Gefundene Muster: {len(results)}")
        match_points = [path['path'][1] for path in results]
        duplicate_points = {point for point in match_points if match_points.count(point) > 1}
        return len(duplicate_points)
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