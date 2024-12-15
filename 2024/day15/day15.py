# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 10092,  # Replace with actual sample answer for part 1
            2: 9021   # Replace with actual sample answer for part 2
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
        self.pos = (0,0)
    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        return [line for line in input_str.split('\n\n')]
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)
    
    @staticmethod
    def expand_boxes(grid):
        expanded = []
        for row in grid:
            new_row = []
            for char in row:
                if char == 'O':
                    new_row.extend(['[', ']'])
                elif char == '@':
                    new_row.extend([char,'.'])
                else:
                    new_row.extend([char, char])
            expanded.append(new_row)
        return expanded
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        
        gps = [[c for c in line] for line in data[0].split('\n')]
        moves = [c for line in data[1] for c in line if c != '\n']
        print(gps)
        print(moves)
        rows = len(gps)
        cols = len(gps[0])
        
        for i in range(rows):
            for j in range(cols):
                if gps[i][j] == '@':
                    self.pos = (i,j)
                    gps[i][j] == '.'
                    break  

        def check_next(direction,x,y):

            dx,dy = self.directions[direction]
            nx,ny = x + 1 * dx, y + 1* dy
            if gps[nx][ny] == '#':
                return False
            if gps[nx][ny] == 'O':
                if check_next(direction,nx,ny):
                    gps[nx][ny],gps[x][y] = gps[x][y],gps[nx][ny]
                    self.pos = (nx,ny)
                    return True     
            if gps[nx][ny] == '.':
                gps[nx][ny],gps[x][y] = gps[x][y],gps[nx][ny]
                self.pos = (nx,ny)
                return True
                
            return False
        for move in moves:
            check_next(move,self.pos[0],self.pos[1])
            pass

        sum = 0
        for r in range(rows):
            for c in range(cols):
                if gps[r][c] == 'O':
                    sum += 100 * r + c
        return sum
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:

        gps = [[c for c in line] for line in data[0].split('\n')]
        moves = [c for line in data[1] for c in line if c != '\n']
        gps = self.expand_boxes(gps)
        rows = len(gps)
        cols = len(gps[0])
        self.print_grid(gps)
        walk = True

        for i in range(rows):
            for j in range(cols):
                if gps[i][j] == '@':
                    x,y= i,j
                    gps[i][j] == '.'
                    break

        for move in moves:
            
            dx,dy = self.directions[move]
            targets = [(x,y)]
            walk = True
            for cr, cc in targets:
                nx,ny = cr + dx, cc + dy
                
                if (nx,ny) in targets: continue
                char = gps[nx][ny]
                if char == '#':
                    walk = False
                if char == '[':
                    targets.append((nx,ny))
                    targets.append((nx,ny+1))   
                if char == ']':
                    targets.append((nx,ny))
                    targets.append((nx,ny-1))
            
            if not walk: continue
            copy = [list(row) for row in gps]
            gps[x][y] = '.'
            gps[x+dx][y+dy] = '@'
            for br,bc in targets[1:]:
                gps[br][bc] = '.'
            for br,bc in targets[1:]:
                gps[br+dx][bc+dy] = copy[br][bc]  
            x += dx
            y += dy

        sum = 0
        for r in range(rows):
            for c in range(cols):
                if gps[r][c] == '[':
                    sum += 100 * r + c
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