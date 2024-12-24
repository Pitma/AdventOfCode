# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 7,  # Replace with actual sample answer for part 1
            2: 'co,de,ka,ta'   # Replace with actual sample answer for part 2
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
        return [[c for c in line.split('-')] for line in input_str.split('\n')]
        return input_str

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

        print("="*100)

    def solve_part1(self, data: Any) -> Union[int, str]:

        starting = dict()

        for pair in data:
            for p in pair:
                if p[0] == 't':
                    if pair[0] not in starting:
                        starting[p] = []
        
        for pair in data:
            if pair[0] in starting:
                starting[pair[0]].append(pair[1])
            if pair[1] in starting:
                starting[pair[1]].append(pair[0])

        final = set()
        for k,v in starting.items():
            for x in range(len(v)-1):
                for y in range(x+1,len(v)):
                    conn = [v[x],v[y]]
                    rconn = [v[y],v[x]]
                    if conn in data: 
                        final.add(tuple(sorted([k,v[x],v[y]])))
                    if rconn in data: 
                        final.add(tuple(sorted([k,v[y],v[x]])))
        
        return len(final)
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        connections = {}
        for x,y in data:
            if x not in connections: 
                connections[x] = set()
            if y not in connections: 
                connections[y] = set()
            connections[x].add(y)
            connections[y].add(x)

        #print(conns)
        sets = set()

        def find_connected(node, others):
            key = tuple(sorted(others))
            if key in sets: return
            sets.add(key)
            for neighbor in connections[node]:
                if neighbor in others: continue
                if not all(neighbor in connections[query] for query in others): continue
                find_connected(neighbor, {*others , neighbor} )

        for c in connections:
            find_connected(c,{c})

        return(','.join(sorted(max(sets, key=len))))
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