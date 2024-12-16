# template.py
from collections import defaultdict, deque, Counter
from typing import Union, List, Dict, Any, Tuple
from pathlib import Path
import re
import heapq

class AoCSolver:
    def __init__(self, level: int = 1):
        self.level = level
        self.sample_answers = {
            1: 11048,  # Replace with actual sample answer for part 1
            2: 64   # Replace with actual sample answer for part 2
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
    def print_path(grid: List[str], path: List[Tuple[int, int, str]], total_cost: int) -> None:
        grid_array = [list(row) for row in grid]

        actions = {'L': 0, 'R': 0, 'F': 0}
        
        print("\nSchritte:")
        for i, (row, col, action) in enumerate(path):
            if action != "START" and grid_array[row][col] not in ['S', 'E']:
                grid_array[row][col] = '*'
            if action in actions:
                actions[action] += 1
            print(f"Schritt {i}: Position ({row}, {col}), Aktion: {action}")
        
        print("\nLabyrinth mit Pfad:")
        for row in grid_array:
            print(''.join(row))
            
        print("\nStatistik:")
        print(f"Gesamtkosten: {total_cost}")
        print(f"Anzahl Schritte gesamt: {len(path) - 1}")
        print(f"Davon:")
        print(f"  Geradeaus (F): {actions['F']}")
        print(f"  Links-Drehungen (L): {actions['L']}")
        print(f"  Rechts-Drehungen (R): {actions['R']}")
        print(f"Drehkosten: {(actions['L'] + actions['R']) * 1000}")
        print(f"Bewegungskosten: {actions['F'] + actions['L'] + actions['R']}")
    @staticmethod

    def print_path2(grid: List[str], path: List[Tuple[int, int, str]], total_cost: int, path_number: int) -> None:
        grid_array = [list(row) for row in grid]

        actions = {'L': 0, 'R': 0, 'F': 0}
        
        print(f"\nPfad {path_number}:")
        for i, (row, col, action) in enumerate(path):
            if action != "START" and grid_array[row][col] not in ['S', 'E']:
                grid_array[row][col] = '*'
            if action in actions:
                actions[action] += 1

        
        print("\nLabyrinth mit Pfad:")
        for row in grid_array:
            print(''.join(row))
            
        print(f"Gesamtkosten: {total_cost}")
        print(f"Anzahl Schritte gesamt: {len(path) - 1}")
        print(f"Davon:")
        print(f"  Geradeaus (F): {actions['F']}")
        print(f"  Links-Drehungen (L): {actions['L']}")
        print(f"  Rechts-Drehungen (R): {actions['R']}")
        print(f"Drehkosten: {(actions['L'] + actions['R']) * 1000}")
        print(f"Bewegungskosten: {actions['F'] + actions['L'] + actions['R']}")
        print("=" * 50)

    @staticmethod
    def find_best_path_low_cost(grid: List[str], turn_cost: int = 1000) -> List[Tuple[int, int, str]]:
        start = end = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    start = (i, j)
                elif grid[i][j] == 'E':
                    end = (i, j)

        if not start or not end:
            return None

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        queue = [(0, start[0], start[1], 1, [(start[0], start[1], "START")])]
        heapq.heapify(queue)
        
        best_costs = defaultdict(lambda: float('inf'))
        best_costs[(start[0], start[1], 1)] = 0

        def can_move_forward(pos_row: int, pos_col: int, dir: int) -> bool:
            next_row = pos_row + directions[dir][0]
            next_col = pos_col + directions[dir][1]
            return (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#')

        while queue:
            total_cost, row, col, facing, path = heapq.heappop(queue)
            if total_cost > best_costs[(row, col, facing)]:
                continue
                
            if (row, col) == end:
                return path, total_cost

            for turn, action in [(-1, "L"), (1, "R")]:
                new_facing = (facing + turn) % 4
                if can_move_forward(row, col, new_facing):
                    next_row = row + directions[new_facing][0]
                    next_col = col + directions[new_facing][1]
                    new_cost = total_cost + turn_cost + 1
                    
                    if new_cost < best_costs[(next_row, next_col, new_facing)]:
                        best_costs[(next_row, next_col, new_facing)] = new_cost
                        new_path = path + [(next_row, next_col, action)]
                        heapq.heappush(queue, (new_cost, next_row, next_col, new_facing, new_path))
            
            if can_move_forward(row, col, facing):
                next_row = row + directions[facing][0]
                next_col = col + directions[facing][1]
                new_cost = total_cost + 1 
                
                if new_cost < best_costs[(next_row, next_col, facing)]:
                    best_costs[(next_row, next_col, facing)] = new_cost
                    new_path = path + [(next_row, next_col, "F")]
                    heapq.heappush(queue, (new_cost, next_row, next_col, facing, new_path))

        return None
    
    @staticmethod
    def find_any_best_paths(grid: List[str], k: int = 3, turn_cost: int = 1000) -> List[Tuple[List[Tuple[int, int, str]], int]]:
        start = end = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    start = (i, j)
                elif grid[i][j] == 'E':
                    end = (i, j)

        if not start or not end:
            return []

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        queue = [(0, start[0], start[1], 1, [(start[0], start[1], "START")])]
        heapq.heapify(queue)
        
        found_paths = []
        
        best_costs = defaultdict(list)
        best_costs[(start[0], start[1], 1)].append(0)

        def can_move_forward(pos_row: int, pos_col: int, dir: int) -> bool:
            next_row = pos_row + directions[dir][0]
            next_col = pos_col + directions[dir][1]
            return (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#')
        
        def is_cost_interesting(state, cost):
            costs = best_costs[state]
            if len(costs) < k:
                return True
            return cost <= max(costs)

        def add_cost(state, cost):
            costs = best_costs[state]
            if len(costs) < k:
                heapq.heappush(costs, -cost) 
            elif cost < -costs[0]: 
                heapq.heapreplace(costs, -cost)

        while queue and len(found_paths) < k:
            total_cost, row, col, facing, path = heapq.heappop(queue)
            
            if (row, col) == end:
                found_paths.append((path, total_cost))
                continue

            for turn, action in [(-1, "L"), (1, "R")]:
                new_facing = (facing + turn) % 4
                if can_move_forward(row, col, new_facing):
                    next_row = row + directions[new_facing][0]
                    next_col = col + directions[new_facing][1]
                    new_cost = total_cost + turn_cost + 1  
                    new_state = (next_row, next_col, new_facing)
                    
                    if is_cost_interesting(new_state, new_cost):
                        add_cost(new_state, new_cost)
                        new_path = path + [(next_row, next_col, action)]
                        heapq.heappush(queue, (new_cost, next_row, next_col, new_facing, new_path))
            
            if can_move_forward(row, col, facing):
                next_row = row + directions[facing][0]
                next_col = col + directions[facing][1]
                new_cost = total_cost + 1  
                new_state = (next_row, next_col, facing)
                
                if is_cost_interesting(new_state, new_cost):
                    add_cost(new_state, new_cost)
                    new_path = path + [(next_row, next_col, "F")]
                    heapq.heappush(queue, (new_cost, next_row, next_col, facing, new_path))

        return found_paths
            
    def solve_part1(self, data: Any) -> Union[int, str]:
        result = self.find_best_path_low_cost(data, turn_cost=0)
        if result:
            path, total_cost = result
            if path:
                print("Kürzester Weg gefunden:")
                self.print_path(data, path, total_cost)
                print(total_cost)
                return total_cost
            else:
                print("Kein Weg gefunden!")
        
        raise NotImplementedError("Part 1 solution not implemented")


    def solve_part2(self, data: Any) -> Union[int, str]:
        paths = self.find_any_best_paths(data, k=100, turn_cost=1000)
        seats = set()
        if paths:
            print(f"Gefundene Wege: {len(paths)}")
            cnt = 0
            mcost = 0
            for i, (path, cost) in enumerate(paths, 1):
                cnt+=1
                if mcost == 0: mcost = cost
                if cost == mcost:
                    for p in path:
                        seats.add((p[0],p[1],'t'))
            self.print_path2(data,seats,cost,99)
        else:
            print("Keine Wege gefunden!")
        print(seats)
        return len(seats)

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