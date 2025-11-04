# template.py
from collections import defaultdict, deque, Counter
from itertools import permutations
import numpy as np
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 330,  # Replace with actual sample answer for part 1
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
            print(' '.join(row))

        print("="*100)

    def ring_score(self,W, tour):
        n = len(tour)
        s = 0
        for k in range(n):
            s += W[tour[k]][tour[(k+1) % n]]
        return s

    def best_ring_exact(self,W):
        n = len(W)
        nodes = list(range(n))
        start = 0                    
        best_tour, best_val = None, float("-inf")

        for perm in permutations(nodes[1:]):  
            tour = (start,) + perm
            if tour[1] > tour[-1]:
                continue
            val = self.ring_score(W, tour)
            if val > best_val:
                best_tour, best_val = tour, val

        return list(best_tour), best_val
    
    def solve_part1(self, data: Any) -> Union[int, str]:
        """Solve part 1 of the puzzle."""
        start = 0
        extracted_data = []
        for line in data:
            match = re.match(r'(^\w+).+(gain|lose).(\d+).+to.(\w+)', line)
            if match:
                person1 = match.group(1)
                gain_lose = match.group(2)
                amount = int(match.group(3))
                person2 = match.group(4)
                if gain_lose == 'lose':
                    amount = -amount

                extracted_data.append((person1, person2, amount))
                
        names = sorted(set(a for a,_,_ in extracted_data) | set(b for _,b,_ in extracted_data))
        name_to_idx = {name: i for i, name in enumerate(names)}

        n = len(names)
        directed = np.zeros((n, n), dtype=float)
        
        for a, b, val in extracted_data:
            i, j = name_to_idx[a], name_to_idx[b]
            directed[i, j] = val

        W_sum = directed + directed.T

        tour, score = self.best_ring_exact(W_sum)

        print("TOUR", [names[i] for i in tour], score)
        return score
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
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
    solver = AoCSolver(level=1)  # Change level
    
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