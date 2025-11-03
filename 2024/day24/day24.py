# template.py
from collections import defaultdict, deque, Counter, OrderedDict
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 2024,  # Replace with actual sample answer for part 1
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

    def solve_part1(self, data: Any) -> Union[int, str]:
        gates = {}
        unknown = {}
        command_list = {}
        for x,y in [line.split(':') for line in data[0].split('\n')]:
            gates[x] = y

        for x,y,z,u in [line.replace("->"," ").split() for line in data[1].split('\n')]:
            #print(x,y,z,u)
            unknown[x,y,z] = [y,u]
            command_list[x,y,z] = [y,u]

        print(unknown)
        unknown = dict(reversed(unknown.items()))
        print(unknown)
        def process(gates,unknown):
            temp = []
            for (gate1,_,gate2),(op,target) in unknown.items():
                if gate1 in gates and gate2 in gates:
                    if op == 'OR':
                        gates[target] = gates[gate1] or gates[gate2]
                    elif op == 'AND':
                        gates[target] = gates[gate1] and gates[gate2]
                    elif op == 'XOR':
                        gates[target] = gates[gate1] != gates[gate2]
                    temp.append([gate1,op,gate2])
                    print([gate1,op,gate2])
                else:
                    print("nope",[gate1,op,gate2])
            
            for (i,o,j) in temp:
                #print(i,j)
                unknown.pop((i,o,j))
            return gates
        
        while unknown != {}:
            print("processing")
            gates = process(gates,unknown)
        
        for (gate1,_,gate2),(op,target) in reversed(command_list.items()):
            if op == 'OR':
                gates[target] = gates[gate1] or gates[gate2]
            elif op == 'AND':
                gates[target] = gates[gate1] and gates[gate2]
            elif op == 'XOR':
                gates[target] = gates[gate1] != gates[gate2]

    
        od = dict(sorted(
            ((k, v) for k, v in gates.items() if k.startswith('z')),
            key=lambda x:int(x[0].replace('z', '').zfill(2)),reverse=True))

        print(od)
        result = ""
        for key, value in od.items():
                    #final[int(key[1:])] = value
                result += str(int(value))

        print(int(result,2))
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