# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re
from operator import xor
from copy import deepcopy

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 0,  # Replace with actual sample answer for part 1
            2: 0   # Replace with actual sample answer for part 2
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
        return [[c for c in line] for line in input_str.split('\n')]
        return input_str
    
    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    @staticmethod
    def find_path_bfs(start, end, grid):

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
    
    @staticmethod
    def find_path_bfs_walls(start, end, grid):

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
                        (grid[new_row][new_col] == '#' or grid[new_row][new_col]=='@') and 
                        (new_row, new_col) not in visited):
                        
                        visited.add((new_row, new_col))
                        new_path = path + [(new_row, new_col)]
                        queue.append(((new_row, new_col), new_path))
            
            return []
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        rows = len(data)
        cols = len(data[0])
        start,end = [],[]

        for i in range(rows):
            for j in range(cols):
                if data[i][j] == 'S':
                    data[i][j] = '.'
                    start = (i,j)
                if data[i][j] == 'E':
                    data[i][j] = '.'
                    end = (i,j)
                    break  
        
        self.print_grid(data)
        print(start,end)
        path = self.find_path_bfs(start,end,data)

        list_walls = set()

        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if data[i][j] == '#':
                    if (data[i+1][j] == '.' and data[i-1][j] == '.') or (data[i][j+1] == '.' and data[i][j-1] == '.'):
                        list_walls.add((i,j)) 
        cnt = 0
        print(len(list_walls))
        print("original Pfad",path)

        for p in range(102,len(path)-1):
            for s in range(len(path)-p):
                pos1 = path[s]
                pos2 = path[s+p] 
                if pos2==(7,5):
                    pass
                if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
                    dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
                    if dist == 2: 
                        wall_pos = ((pos1[0] + pos2[0])//2, (pos1[1] + pos2[1])//2)
                        if wall_pos in list_walls:
                            cnt += 1
        return cnt
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        rows = len(data)
        cols = len(data[0])

        for i in range(rows):
            for j in range(cols):
                if data[i][j] == 'S':
                    break
            else:
                continue
            break  
        
        distance = [[-1]* cols for _ in range(rows)]
        distance[i][j] = 0

        q = deque([(i,j)])
        while q:
            cr,cc = q.popleft()
            for nr,nc in [(cr+1,cc), (cr-1,cc),(cr,cc+1),(cr,cc -1)]:
                if nr < 0 or cc <0 or nr>= rows or nc >= cols: continue
                if data[nr][nc] == "#": continue
                if distance[nr][nc] != -1: continue
                distance[nr][nc] = distance[cr][cc] + 1
                q.append((nr,nc))

        count = 0

        for r in range(rows):
            for c in range(cols):
                if data[r][c] == "#":continue
                for lookup in range(2,21):
                    for dr in range(lookup + 1):
                        dc = lookup - dr
                        for nr,nc in {(r + dr,c + dc),(r + dr, c - dc), (r - dr, c + dc),(r - dr,c - dc)}:
                            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                            if data[nr][nc] == "#": continue
                            if distance[r][c] - distance[nr][nc] >= 100 + lookup: count += 1

        print(count)

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
    # sample_input = solver.read_file("sample.txt")
    # sample_answer = solver.solve(sample_input)
    # expected = solver.sample_answers[solver.level]
    
    # print(f"Sample answer: {sample_answer}")
    # assert sample_answer == expected, f"Expected {expected}, got {sample_answer}"
    
    # Solve
    input_data = solver.read_file("input.txt")
    answer = solver.solve(input_data)
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()