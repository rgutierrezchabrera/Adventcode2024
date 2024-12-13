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
    region_char = grid[start[0]][start[1]]  # Character of the region we're exploring
    region_cells = {start}  # Set to track cells in the current region
    visited.add(start)  # Mark the starting cell as visited

    # Directions for movement (Down, Up, Right, Left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
    while queue:
        next_queue = []
        for row, col in queue:
            for d_row, d_col in directions:
                neighbor_row, neighbor_col = row + d_row, col + d_col
                if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]) and grid[neighbor_row][neighbor_col] == region_char:
                    if (neighbor_row, neighbor_col) not in visited:
                        visited.add((neighbor_row, neighbor_col))
                        region_cells.add((neighbor_row, neighbor_col))
                        next_queue.append((neighbor_row, neighbor_col))
        queue = next_queue
    return region_cells

# Calculate the sides of a given region
def calculate_sides(region: Set[Tuple[int, int]], grid: List[str]) -> int:
    sides = 0
    edge = set()  # Track edges we've already processed
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Directions (Down, Up, Right, Left)

    # Iterate through each cell in the region
    for row, col in region:
        for d_row, d_col in directions:
            # Calculate the position of the neighbor in the given direction
            neighbor_row, neighbor_col = row + d_row, col + d_col
            if (neighbor_row, neighbor_col) not in region and (row, col, d_row, d_col) not in edge:
                sides += 1  # This is an exposed side, so we count it
                update = True
                edge.add((row, col, d_row, d_col))  # Mark this edge as processed
                local = set()
                local.add((row, col, d_row, d_col))  # Start tracking this edge
                i = 1
                while update:
                    update = False
                    # Check in the "next" direction (move forward)
                    next_row, next_col = row + d_col * i, col + d_row * i  # 'next_row' and 'next_col' for moving forward
                    next_row1, next_col1 = next_row + d_row, next_col + d_col  # Check next position in the direction
                    if (next_row, next_col) in region and (next_row1, next_col1) not in region and (next_row, next_col, d_row, d_col) not in edge:
                        edge.add((next_row, next_col, d_row, d_col))  # Add this "next" edge
                        local.add((next_row, next_col, d_row, d_col))
                        update = True
                    i += 1
                i = 1
                update = True
                while update:
                    update = False
                    # Check in the "previous" direction (move backward)
                    prev_row, prev_col = row - d_col * i, col - d_row * i  # 'prev_row' and 'prev_col' for moving backward
                    prev_row1, prev_col1 = prev_row + d_row, prev_col + d_col  # Check next position in the opposite direction
                    if (prev_row, prev_col) in region and (prev_row1, prev_col1) not in region and (prev_row, prev_col, d_row, d_col) not in edge:
                        edge.add((prev_row, prev_col, d_row, d_col))  # Add this "previous" edge
                        local.add((prev_row, prev_col, d_row, d_col))
                        update = True
                    i += 1
    return sides

def part2() -> int:
    grid = read_input()  # Read the input grid
    visited = set()  # Set to track visited cells
    total_result = 0  # Variable to store the result

    # Iterate over each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = (row, col)
            if cell not in visited:
                # Find all cells in the current region using BFS
                region_cells = bfs_find_region(cell, visited, grid)
                # Calculate the number of exposed sides for the region
                sides = calculate_sides(region_cells, grid)
                # Add the contribution of this region to the total result
                total_result += len(region_cells) * sides
                
    return total_result

# Run Part 2
if __name__ == "__main__":
    print("--- Part Two ---")
    print("Answer: " + str(part2()))
