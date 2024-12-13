import sys
from typing import List, Set, Tuple

# Read the input from a file or standard input
def read_input() -> List[str]:
    try:
        with open("input.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return [line.strip() for line in sys.stdin.readlines()]

# Perform a breadth-first search to find all cells in a contiguous region
def bfs_find_region(start: Tuple[int, int], visited: Set[Tuple[int, int]], grid: List[str]) -> Set[Tuple[int, int]]:
    queue = [start]
    region_char = grid[start[0]][start[1]]
    region_cells = {start}  # Track all cells in the region
    visited.add(start)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    while queue:
        next_queue = []
        for row, col in queue:
            for d_row, d_col in directions:
                neighbor_row, neighbor_col = row + d_row, col + d_col
                # Ensure the neighbor is within bounds and matches the region's character
                if (
                    0 <= neighbor_row < len(grid) and
                    0 <= neighbor_col < len(grid[0]) and
                    grid[neighbor_row][neighbor_col] == region_char
                ):
                    neighbor = (neighbor_row, neighbor_col)
                    if neighbor not in visited:
                        visited.add(neighbor)
                        region_cells.add(neighbor)
                        next_queue.append(neighbor)
        queue = next_queue

    return region_cells

# Calculate the perimeter of a given region
def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[str]) -> int:
    perimeter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    for row, col in region:
        for d_row, d_col in directions:
            neighbor_row, neighbor_col = row + d_row, col + d_col
            if not (0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0])):
                # Out of bounds is considered perimeter
                perimeter += 1
            elif (neighbor_row, neighbor_col) not in region:
                # Adjacent to a different region is also perimeter
                perimeter += 1

    return perimeter

# Part 1 logic
def part1() -> int:
    grid = read_input()
    visited = set()
    total_result = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = (row, col)
            if cell not in visited:
                # Find all cells in the current region
                region_cells = bfs_find_region(cell, visited, grid)
                # Calculate the perimeter of the region
                perimeter = calculate_perimeter(region_cells, grid)
                # Add the region's contribution to the total result
                total_result += len(region_cells) * perimeter

    return total_result

# Run Part 1
if __name__ == "__main__":
    print("--- Part One ---")
    print("Answer: " + str(part1()))
