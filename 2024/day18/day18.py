# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 22,  # Replace with actual sample answer for part 1
            2: None   # Replace with actual sample answer for part 2
        }
        
        # Common direction vectors
        self.directions = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1)
        }

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        # return [line for line in input_str.split('\n')]
        # return [int(line) for line in input_str.split('\n')]
        return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def find_path_bfs(grid):
            start = (0,0)
            end = (70,70)

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            queue = deque([(start, [start])])
            visited = {start}
            while queue:
                (row, col), path = queue.popleft()

                if (row, col) == end:
                    return path
                
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    
                    if (0 <= new_row < len(grid) and 
                        0 <= new_col < len(grid[0]) and 
                        grid[new_row][new_col] != '#' and 
                        (new_row, new_col) not in visited):
                        
                        visited.add((new_row, new_col))
                        new_path = path + [(new_row, new_col)]
                        queue.append(((new_row, new_col), new_path))
            
            return [] 
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        rows = 71
        cols = 71
        print(data)
        maze = [['.']*cols for i in range(rows)]

        for i in range(1025):
            (corrupt_c,corrupt_r) = data[i]
            maze[corrupt_r][corrupt_c] = '#'
        
        self.print_grid(maze)
        way = list(map(list,self.find_path_bfs(maze)))
        for x,y in way:
            maze[x][y] = 'O'
        self.print_grid(maze)
        return len(way) -1
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        rows = 71
        cols = 71
        print(data)
        maze = [['.']*cols for i in range(rows)]

        cycle = 0
        for i in range(len(data)):
            (corrupt_c,corrupt_r) = data[i]
            maze[corrupt_r][corrupt_c] = '#'
            if i < 1025: continue
            way = list(map(list,self.find_path_bfs(maze)))
            if  way == []:
                return corrupt_c,corrupt_r
        
        return cycle

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
    #sample_input = solver.read_file("sample.txt")
    #sample_answer = solver.solve(sample_input)
    #expected = solver.sample_answers[solver.level]
    
    #print(f"Sample answer: {sample_answer}")
    #assert sample_answer == expected, f"Expected {expected}, got {sample_answer}"
    
    # Solve
    input_data = solver.read_file("input.txt")
    answer = solver.solve(input_data)
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()