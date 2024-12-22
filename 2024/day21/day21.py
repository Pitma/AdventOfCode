# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
from itertools import product
from functools import cache

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 126384,  # Replace with actual sample answer for part 1
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

    def parse_input(self, input_str: str) -> Any:
        """Parse input string into desired format."""
        # Common parsing patterns - uncomment as needed
        return [line for line in input_str.split('\n')]
        # return [int(line) for line in input_str.split('\n')]
        # return [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.split('\n')]
        # return [[c for c in line] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(str(row)))

        print("="*100)

    def solve_part1(self, data: Any) -> Union[int, str]:
        arrows = [[None,'^','A'],
                  ['<','v','>']]

        numpads = [['7','8','9'],
                   ['4','5','6'],
                   ['1','2','3'],
                   [None,'0','A']]
        
        def solve(string,grid):
            pos = {}
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] is not None: pos[grid[r][c]] = (r,c)
            seqs = {}
            for x in pos:
                for y in pos:
                    if x == y:
                        seqs[(x,y)] = ['A']
                        continue
                    possibilities = []
                    q = deque([(pos[x],"")])
                    optimal = float("inf")

                    while q: 
                        (r,c), moves = q.popleft()
                        for nr,nc,nm in [(r-1,c,'^'),(r+1,c,'v'),(r,c-1,'<'),(r,c+1,'>')]:
                            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) : continue
                            if grid[nr][nc] is None: continue
                            if grid[nr][nc] == y:
                                if optimal < len(moves) + 1:break
                                optimal = len(moves) + 1
                                possibilities.append(moves + nm + 'A')
                            else:
                                q.append(((nr,nc),moves + nm))
                        else:
                            continue
                        break

                    seqs[(x,y)] = possibilities
            options = [seqs[(x,y)] for x,y in zip('A'+ string,string)]
            return [''.join(x) for x in product(*options)]

        def solve_loop(sequences):
            possible_robot = []
            for seq in sequences:
                possible_robot += solve(seq,arrows)
            minlen = min(map(len, possible_robot))
            return [seq for seq in possible_robot if len(seq) == minlen],minlen


        sum = 0

        for d in data:
            robots = 2
            robot1 = solve(d,numpads)
            possible = robot1
            minimum = 0
            for i in range(robots):
                possible,minimum = solve_loop(possible)
            
            sum += int(d[:-1]) * minimum
        return sum
    
    
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:

        def compute_seq(grid):
            pos = {}
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] is not None: pos[grid[r][c]] = (r,c)
            seqs = {}
            for x in pos:
                for y in pos:
                    if x == y:
                        seqs[(x,y)] = ['A']
                        continue
                    possibilities = []
                    q = deque([(pos[x],"")])
                    optimal = float("inf")

                    while q: 
                        (r,c), moves = q.popleft()
                        for nr,nc,nm in [(r-1,c,'^'),(r+1,c,'v'),(r,c-1,'<'),(r,c+1,'>')]:
                            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) : continue
                            if grid[nr][nc] is None: continue
                            if grid[nr][nc] == y:
                                if optimal < len(moves) + 1:break
                                optimal = len(moves) + 1
                                possibilities.append(moves + nm + 'A')
                            else:
                                q.append(((nr,nc),moves + nm))
                        else:
                            continue
                        break

                    seqs[(x,y)] = possibilities
            return seqs
        
        def solve(string,seqs):
            options = [seqs[(x,y)] for x,y in zip('A'+ string,string)]
            return [''.join(x) for x in product(*options)]

        numpads = [['7','8','9'],
                   ['4','5','6'],
                   ['1','2','3'],
                   [None,'0','A']]
        num_seq = compute_seq(numpads)

        arrows = [[None,'^','A'],
                  ['<','v','>']]

        arrow_seq = compute_seq(arrows)
        arrow_lengths = {key: len(value[0]) for key, value in arrow_seq.items()} 


        @cache
        def compute_length(x,y,depth=25):
            if depth == 1:
                return arrow_lengths[(x,y)]
            optimal = float("inf")
            for seq in arrow_seq[(x,y)]:
                length = 0
                for a,b in zip('A'+ seq, seq):
                    length += compute_length(a,b,depth - 1)
                optimal = min(optimal,length)
            return optimal
        
        
        sum = 0

        for d in data:
            inputs = solve(d,num_seq)
            optimal = float("inf")
            for seq in inputs:
                length = 0
                for x,y in zip('A' + seq,seq):
                    length += compute_length(x,y)
                optimal = min(optimal,length)
            sum += int(d[:-1]) * optimal

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