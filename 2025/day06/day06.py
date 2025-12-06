# template.py
from collections import defaultdict, deque, Counter
from io import StringIO
from typing import Union, List, Dict, Any
from pathlib import Path
import re
import ast
import pandas as pd

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 4277556,  # Replace with actual sample answer for part 1
            2: 3263827   # Replace with actual sample answer for part 2
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
        #return [line.split() for line in input_str.split('\n')]
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
        """Solve part 1 of the puzzle."""
        data = [line.split() for line in data.split('\n')]
        operations =[]
        for i in range(len(data[0])):
                operations.append([line[i] for line in data])
        result = 0
        print(operations)
        for op in operations:
                math = ''
                for i in range(len(op)-2):
                    math = math + ' ' + op[i] + ' ' + op[len(op)-1] 
                math = math + ' ' + op[len(op)-2]
                print(math)
                result += eval(math)
        return result
                
        raise NotImplementedError("Part 1 solution not implemented")

    def solve_part2(self, data: Any) -> Union[int, str]:
        """Solve part 2 of the puzzle."""
        check_data = [line for line in data.split('\n')]
        max_len = check_data[0]
        new_data = data.split('\n')
        print("new_data:", new_data)
        data = []
        #print("check_data:", check_data)
        for i in range(len(check_data[0])):
            tmp_op = ''
            tmp_list = ''
            for j in range(len(max_len)):
                #print(new_data[j][i])
                try:    
                        if new_data[j][i] != '*' and new_data[j][i] != '+':
                            tmp_op += new_data[j][i]
                except:
                        continue
            tmp_list +=tmp_op
            #print("tmp_list:", tmp_list)
            data.append(tmp_list)
        print("data:", data)
        """ group_size = 0
        for item in data:
            if item.strip() == '':
                break
            group_size += 1 """
        grouped_data = []
        current_group = []
        cleaned_data = [item.strip() for item in data if item.strip() != '']
        for item in data:

            cleaned_item_for_check = item.strip()
            if cleaned_item_for_check == '':
                if current_group:
                    grouped_data.append(current_group)
                    current_group = []
            else:
                cleaned_number_str = cleaned_item_for_check.replace(' ', '')
                current_group.append(cleaned_number_str)
        if current_group:
            grouped_data.append(current_group)

        print("grouped_data:", grouped_data)
        print("cleaned_data:", cleaned_data)
        final_data = []   
        operators = new_data[-1].replace(' ', '')
        for m in range(len(grouped_data)):
            grouped_data[m].append(operators[m].replace(' ', ''))

        print("final grouped_data:", grouped_data)
        """ raise NotImplementedError("Part 2 solution not implemented")
        operations =[]
        new_operations = []
        for i in range(len(data[0])):
                operations.append([line[i] for line in data])
        result = 0
        print(operations)
        for op in operations:
            max_len = max(op,key=len)
            tmp_list = []
            for p in range(len(max_len)):
                tmp_op = ''
                for i in range(len(op)-1):
                    try:
                        tmp_op += op[i][p]
                    except:
                        continue
                tmp_list.append(tmp_op)
            tmp_list.append(op[-1])
            new_operations.append(tmp_list)
          """
        result = 0     
        for op in grouped_data:
                math = ''
                for i in range(len(op)-2):
                    math = math + ' ' + op[i] + ' ' + op[len(op)-1] 
                math = math + ' ' + op[len(op)-2]
                #print(math)
                result += eval(math)
                #print("result:", eval(math))
        if result < 23177300295750:
            return result 
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