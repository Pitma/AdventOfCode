# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any
from pathlib import Path
import re

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: '4,6,3,5,6,3,5,2,1,0',  # Replace with actual sample answer for part 1
            2: 109019930331546   # Replace with actual sample answer for part 2
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


    def solve_part1(self, data: Any) -> Union[int, str]:
        registers = [int(x) for x in re.findall(r'-?\d+', data[0])]
        program = [int(x) for x in data[1].split(': ')[1].split(',')]
        print("Registers",registers)
        print("Program:", program)
        output = []
        combo = {0:0,1:1,2:2,3:3,4:registers[0],5:registers[1],6:registers[2]}

        pos = 0

        while True:
            if pos >= len(program):
                break
            combo = {0:0,1:1,2:2,3:3,4:registers[0],5:registers[1],6:registers[2],7:0}
            opcode = program[pos]
            operand = program[pos+1]
            combo_operand = combo[operand]
            if opcode == 0:
                print("adv")
                registers[0] = registers[0] >> combo_operand
                print(registers)
                pos += 2
                continue
            if opcode == 1:
                print("bxl", registers[1] ^ operand)
                registers[1] =  registers[1] ^ operand
                pos += 2
                continue
            if opcode == 2:
                print("bst", pos)
                registers[1] = combo_operand % 8
                pos +=2
                continue
            if opcode == 3:
                print("jnz", pos)
                if registers[0] == 0:
                    pos += 2
                    continue
                pos = operand
                continue
            if opcode == 4:
                print("bxc",pos)
                registers[1] = registers[1] ^ registers[2]
                pos += 2
                continue
            if opcode == 5:
                print("out",combo_operand%8)
                print(output)
                output.append(','.join(str(combo_operand%8)))
                print(output)
                pos +=2
                continue
            if opcode == 6:
                print("bdv",pos)
                registers[1] = registers[0] >> combo_operand
                print(registers)
                pos += 2
                continue
            if opcode == 7:
                print("cdv",pos)
                registers[2] = registers[0] >> combo_operand
                print(registers)
                pos += 2
                continue
        print('Result:')
        return ','.join([x for x in output])
            

        raise NotImplementedError("Part 1 solution not implemented")


    def solve_part2(self, data: Any) -> Union[int, str]:
        registers = [0]*3
        program = [int(x) for x in data[1].split(': ')[1].split(',')]
        print("Registers",registers)
        print("Program:", program)

        def find(program,answer):
            print(program,answer)
            if program == []: return answer
            for t in range(8):
                a = answer << 3 | t
                b = a % 8
                b = b ^ 5
                c = a >> b
                b = b ^ c
                b = b ^ 6
                if b % 8 == program[-1]:
                    sub = find(program[:-1],a)
                    if sub is None: continue
                    return sub
                
        return find(program,0)

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