# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any, Tuple
from pathlib import Path
import time

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 41,  # Replace with actual sample answer for part 1
            2: 6   # Replace with actual sample answer for part 2
        }
        
        # Common direction vectors
        self.directions = {
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1),
            'NE': (-1, 1),
            'SE': (1, 1),
            'SW': (1, -1),
            'NW': (-1, -1)
        }

        self.next_direction = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        # return [line for line in input_str.split('\n')]
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        return [[c for c in line] for line in input_str.split('\n')]
        return input_str


    def find_starting_point_and_direction(self, room: List[List[str]]) -> Tuple[List[int], str]:
        for i, row in enumerate(room):
            for j, cell in enumerate(row):
                if cell not in '.#O':
                    return [i, j], cell
        raise ValueError("No starting point found in room")

    def find_path(self, data: List[List[str]]) -> Tuple[List[List[int]], bool]:
        position, curr_direction = self.find_starting_point_and_direction(data)
        visited = []
        save_point = []
        start_time = time.monotonic()
        
        def is_valid_position(x: int, y: int) -> bool:
            return 0 <= x < len(data) and 0 <= y < len(data[0])

        while True:
            if time.monotonic() - start_time > 0.02:
                return visited, True
                
            x, y = position
            visited.append([x, y])
            
            dx, dy = self.directions[curr_direction]
            next_x, next_y = x + dx, y + dy
            
            if not is_valid_position(next_x, next_y):
                return visited, False
                
            if data[next_x][next_y] == 'O':
                if [x, y] == save_point:
                    return visited, True
                if not save_point:
                    save_point = [x, y]
                    
            if data[next_x][next_y] in '#O':
                curr_direction = self.next_direction[curr_direction]
                continue
                
            position = [next_x, next_y]

    def solve_part1(self, data: List[List[str]]) -> int:
        visited, _ = self.find_path(data)
        return len(list({tuple(x) for x in visited}))
    
        raise NotImplementedError("Part 1 solution not implemented")


    def solve_part2(self, data: Any) -> Union[int, str]:
        visited, _ = self.find_path(data)
        start_pos, _ = self.find_starting_point_and_direction(data)
        visited_unique = list({tuple(x) for x in visited})
        visited_unique.remove(tuple(start_pos))
        
        count = 0
        for x, y in visited_unique:
            new_data = [row[:] for row in data]
            new_data[x][y] = 'O'
            _, is_loop = self.find_path(new_data)
            if is_loop:
                count += 1
        return count
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