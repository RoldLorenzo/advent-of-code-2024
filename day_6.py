from util import *
from dataclasses import dataclass

DIRECTIONS = [
    (-1, 0), # up
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
]

@dataclass
class Path:
    # Stores all distinct positions visited along the path.
    # Each key is a coordinate (x, y), and the corresponding value is a set of directions
    # from which the path entered that position.
    # Tracking directions at each position will be useful for detecting loops.
    positions_visited: dict[tuple[int, int], set[int]]
    stuck_in_a_loop: bool

class PathSimulator:
    def __init__(self, guard_map: list[list[str]]):
        self.guard_map = guard_map
        
        self.i, self.j = self.get_init_position()
        self.dir_index = 0
    
    def get_init_position(self) -> tuple[int, int]:
        for i, row in enumerate(self.guard_map):
            for j, tile in enumerate(row):
                if tile == "^": return (i, j)
            
        raise RuntimeError("Guard position not in the map!")
    
    def turn(self):
        self.dir_index = (self.dir_index + 1) % len(DIRECTIONS)
    
    def position_in_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < len(self.guard_map) and 0 <= j < len(self.guard_map[i])
    
    def simulate_path(self) -> Path:
        path = Path({}, False)
        
        while True:
            dir = DIRECTIONS[self.dir_index]
            
            curr_position = (self.i, self.j)
            
            path.positions_visited.setdefault(curr_position, set())
            directions_visited = path.positions_visited[curr_position]
            
            # If I already entered this position, through this direction, I'm in a loop.
            if self.dir_index in directions_visited:
                path.stuck_in_a_loop = True
                return path
            
            directions_visited.add(self.dir_index)
            
            new_i = self.i + dir[0]
            new_j = self.j + dir[1]
            
            if not self.position_in_bounds(new_i, new_j):
                return path
            
            if self.guard_map[new_i][new_j] == "#":                
                self.turn()
                continue
            
            self.i = new_i
            self.j = new_j

def count_possible_loops(guard_map: list[list[str]], path: Path) -> int:
    possible_loops = 0
    
    for (i, j) in path.positions_visited:
        if guard_map[i][j] == "^":
            continue
        
        # Place an obstacle in this position and check if it will result in a loop.
        guard_map[i][j] = "#"
        
        path_simulator = PathSimulator(guard_map)
        theoretical_path = path_simulator.simulate_path()
        
        if theoretical_path.stuck_in_a_loop:
            possible_loops += 1
        
        # Remove old obstacle.
        guard_map[i][j] = "."
            
    return possible_loops

if __name__ == "__main__":
    guard_map = list(map(list, file_lines()))
    
    path_simulator = PathSimulator(guard_map)
    path = path_simulator.simulate_path()
    
    part_one = len(path.positions_visited)
    part_two = count_possible_loops(guard_map, path)
    
    print_results(part_one, part_two)