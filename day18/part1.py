import sys
from collections import deque

# Movement directions: (row, col)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse_input(input_data):
    """
    Parse the input into a list of (x, y) coordinates.
    """
    return [tuple(map(int, line.split(','))) for line in input_data.strip().splitlines()]

def create_corrupted_grid(corrupted_positions, grid_size):
    """
    Create a grid with corrupted positions marked as '#'.
    """
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in corrupted_positions:
        grid[y][x] = '#'  # Mark corrupted positions
    return grid

def calculate_shortest_path(grid, grid_size):
    """
    Calculate the shortest path from the top-left corner to the bottom-right corner using BFS.
    """
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    queue = deque([(start, 0)])  # ((row, col), steps)
    visited = set()
    visited.add(start)

    while queue:
        (row, col), steps = queue.popleft()

        if (row, col) == end:
            return steps  # Found the shortest path

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size and (nr, nc) not in visited and grid[nr][nc] == '.':
                visited.add((nr, nc))
                queue.append(((nr, nc), steps + 1))

    return -1  # No path found

def main():
    """
    Main function to calculate the shortest path in the memory grid.
    """
    # Example input and grid size
    example_input = """
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    1,5
    0,6
    3,3
    2,6
    5,1
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    6,1
    1,0
    0,5
    1,6
    2,0
    """
    example_grid_size = 7
    example_corrupted = parse_input(example_input)
    example_grid = create_corrupted_grid(example_corrupted[:12], example_grid_size)
    example_result = calculate_shortest_path(example_grid, example_grid_size)

    if example_result == 22:
        print("Test works! Example result:", example_result)
    else:
        print("Test failed. Example result:", example_result)
        return

    # File input and full grid size
    full_grid_size = 71
    with open('input.txt') as f:
        input_corrupted = parse_input(f.read())

    full_grid = create_corrupted_grid(input_corrupted[:1024], full_grid_size)
    full_result = calculate_shortest_path(full_grid, full_grid_size)

    print("Result for the input file:", full_result)

if __name__ == "__main__":
    main()
