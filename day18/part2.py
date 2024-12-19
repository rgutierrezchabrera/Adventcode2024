import sys
from collections import deque

# Movement directions: (row, col)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse_input(input_data):
    """
    Parse the input into a list of (x, y) coordinates.
    """
    return [tuple(map(int, line.split(','))) for line in input_data.strip().splitlines()]

def create_corrupted_grid(corrupted_positions, grid_size, step):
    """
    Create a grid with corrupted positions up to the given step.
    """
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in corrupted_positions[:step]:
        grid[y][x] = '#'  # Mark corrupted positions
    return grid

def is_path_blocked(grid, grid_size):
    """
    Check if a path exists from the top-left corner to the bottom-right corner using BFS.
    """
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        row, col = queue.popleft()

        if (row, col) == end:
            return False  # Path exists

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size and (nr, nc) not in visited and grid[nr][nc] == '.':
                visited.add((nr, nc))
                queue.append((nr, nc))

    return True  # Path is blocked

def find_first_blocking_byte(corrupted_positions, grid_size):
    """
    Find the first corrupted byte that blocks the path to the exit using binary search.
    """
    left, right = 0, len(corrupted_positions) - 1
    first_blocking_byte = None
    while left <= right:
        mid = (left + right) // 2
        # Create the grid for the mid step
        grid = create_corrupted_grid(corrupted_positions, grid_size, mid + 1)
        
        if is_path_blocked(grid, grid_size):
            # If path is blocked, mid might be the first blocking byte
            first_blocking_byte = corrupted_positions[mid]
            # Search in the left half for earlier blocking bytes
            right = mid - 1
        else:
            # Path is not blocked, search in the right half
            left = mid + 1
    return first_blocking_byte

def main():
    """
    Main function to find the first blocking byte in the memory grid.
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
    example_result = find_first_blocking_byte(example_corrupted, example_grid_size)

    if example_result == (6, 1):
        print("Test works! Example result:", example_result)
    else:
        print("Test failed. Example result:", example_result)
        return

    # File input and full grid size
    full_grid_size = 71
    with open('input.txt') as f:
        input_corrupted = parse_input(f.read())

    full_result = find_first_blocking_byte(input_corrupted, full_grid_size)

    print(f"{full_result[0]},{full_result[1]}")

if __name__ == "__main__":
    main()
