import sys
import re
from collections import deque
import pyperclip as pc

def print_and_copy(s):
    """Print the result and copy it to clipboard."""
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

def extract_integers(s):
    """Extract all integers from a string, including negative numbers."""
    return [int(x) for x in re.findall(r'-?\d+', s)]

# Read input file
input_file = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
data = open(input_file).read().strip()

GRID_WIDTH = 101
GRID_HEIGHT = 103

robots = []

# Parse robot data from input
for line in data.split('\n'):
    px, py, vx, vy = extract_integers(line)
    robots.append((px, py, vx, vy))

# Set to keep track of previously seen grids
seen_grids = set()

# Main simulation loop
for time_step in range(1, 10**6):
    # Initialize grid
    grid = [['.' for y in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]
    
    # Update robot positions
    for i, (px, py, vx, vy) in enumerate(robots):
        px = (px + vx) % GRID_WIDTH
        py = (py + vy) % GRID_HEIGHT
        robots[i] = (px, py, vx, vy)
        grid[px][py] = '#'

    # Count robots and connected components
    robot_count = sum(row.count('#') for row in grid)
    components = 0
    visited = set()

    # BFS to find connected components
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == '#' and (x, y) not in visited:
                components += 1
                queue = deque([(x, y)])
                while queue:
                    x2, y2 = queue.popleft()
                    if (x2, y2) in visited:
                        continue
                    visited.add((x2, y2))
                    for dx, dy in DIRECTIONS:
                        xx, yy = x2 + dx, y2 + dy
                        if 0 <= xx < GRID_WIDTH and 0 <= yy < GRID_HEIGHT and grid[xx][yy] == '#':
                            queue.append((xx, yy))
    
    # Check if the current grid configuration is new
    grid_tuple = tuple(tuple(row) for row in grid)
    if grid_tuple not in seen_grids:
        seen_grids.add(grid_tuple)
        if time_step % 1000 == 0:
            print(f"Time step: {time_step}")
        if components <= 350:
            print(f"Interesting configuration at time step: {time_step}")
            grid_string = '\n'.join(''.join(grid[x][y] for x in range(GRID_WIDTH)) for y in range(GRID_HEIGHT))
            print(grid_string)