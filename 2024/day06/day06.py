# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
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


    def find_starting_point_and_direction(self,room):
        for i in (range(len(room))):
            for j in (range(len(room[i]))):
                if room[i][j] not in ['.','#','O']:
                    return [i,j],room[i][j]

    def find_path(self, data: Any):
        visited = []
        rows = len(data)
        cols = len(data[0])
        isLoop = False
        save_point = []

        position,curr_direction = AoCSolver.find_starting_point_and_direction(self, data)

        def is_valid_position(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def turn_right(curr_direction):
            return self.next_direction[curr_direction]

        def check_next_pos(start_x, start_y,direction,save_point):
            (dx,dy) = self.directions[direction]
            next_x = start_x + 1 * dx
            next_y = start_y + 1 * dy
            curr_direction = direction
            
            if not is_valid_position(next_x, next_y):
                return None
            
            if data[next_x][next_y] == 'O' and [start_x,start_y] == save_point:
                return [next_x,next_y],curr_direction,save_point, True
            
            if data[next_x][next_y] == 'O' and save_point == []:
                save_point = [start_x,start_y]

            if data[next_x][next_y] == '#' or data[next_x][next_y] == 'O':
                curr_direction = turn_right(curr_direction)
                return [start_x,start_y],curr_direction,save_point,False

            return [next_x,next_y],curr_direction,save_point,False
        
        start_time = time.monotonic()
        while True:
            try:
                position,curr_direction,save_point,isLoop = check_next_pos(position[0],position[1],curr_direction,save_point)
                visited.append(position)
                if isLoop:
                    break
                end_time = time.monotonic()
                elapsed_time = end_time - start_time
                if elapsed_time > 0.02:
                    isLoop = True
                    break
                
            except TypeError:
                break

        return list(map(list, dict.fromkeys(map(tuple,visited)))), isLoop


    def solve_part1(self, data: Any) -> Union[int, str]:
        visited = AoCSolver.find_path(self, data)
        #print(visited)
        return len(visited)
    
        raise NotImplementedError("Part 1 solution not implemented")


    def solve_part2(self, data: Any) -> Union[int, str]:
        cnt = 0
        possible_locations,_ = AoCSolver.find_path(self, data)
        position,_ = AoCSolver.find_starting_point_and_direction(self, data)
        possible_locations.remove(position)
        
        for location in possible_locations:
            new_data = list(map(list,data))
            new_data[location[0]][location[1]] = "O"
            _,isLoop = AoCSolver.find_path(self, new_data)
            
            if isLoop:
                cnt +=1 

        return cnt
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