# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 12,  # Replace with actual sample answer for part 1
            2: None   # Replace with actual sample answer for part 2
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
        self.fullsize = False
    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        # return [line for line in input_str.split('\n')]
        # return [int(line) for line in input_str.split('\n')]
        return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    def solve_part1(self,data: Any) -> Union[int, str]:
        if self.fullsize:
            width, height = 101,103
        else:
            width, height = 11,7 
        seconds = 100
        end_positions = []
        for robot in data:
            x,y,xv,yv = robot
            steps = x + xv * seconds
            while steps < 0:
                steps+=width
            pos_x = steps % width
            steps = y + yv * seconds
            while steps < 0:
                steps+=height
            pos_y = steps % height

            end_positions.append([pos_x,pos_y])
        q1 = len([pos for pos in end_positions if pos[0] < (width-1)/2 and pos[1] < (height-1)/2])
        q2 = len([pos for pos in end_positions if pos[0] > (width-1)/2 and pos[1] < (height-1)/2])
        q3 = len([pos for pos in end_positions if pos[0] < (width-1)/2 and pos[1] > (height-1)/2])
        q4 = len([pos for pos in end_positions if pos[0] > (width-1)/2 and pos[1] > (height-1)/2])

        self.fullsize = True
        return q1*q2*q3*q4
        raise NotImplementedError("Part 1 solution not implemented")

    @staticmethod
    def print_grid(koordinaten):
        grid = [['.' for _ in range(101)] for _ in range(103)]
        
        for x, y in koordinaten:
            if 0 <= x < 101 and 0 <= y < 103:
                grid[y][x] = '#'
        
        for zeile in grid:
            print(''.join(zeile))
        print("="*100)
        

    def solve_part2(self, data: Any) -> Union[int, str]:

        width, height = 101,103
       
        seconds = 6888 # final result for quicker showcase -> set to 0 for clean run
        while True:
            if seconds >9999: # in my case 10000 was too high
                print("nothing found") 
                break
            if seconds % 1000 == 0: # show current status of seconds
                print(seconds)
            end_positions = []
            for robot in data:
                x,y,xv,yv = robot
                steps = x + xv * seconds
                while steps < 0:
                    steps+=width
                pos_x = steps % width
                steps = y + yv * seconds
                while steps < 0:
                    steps+=height
                pos_y = steps % height

                end_positions.append([pos_x,pos_y])
            
            
            count = 0

            for (x,y) in end_positions:
                if [width-x,y] in end_positions:
                    count += 1 
            
            if count >len(data)/4: # most of the robots are mirrored
                print(seconds)
                self.print_grid(end_positions)
                break
            seconds +=1

        return seconds
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
    level = 2 # Change level
    solver = AoCSolver(level)
    
    # Test
    if level == 1: #no test in level 2
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