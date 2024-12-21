from collections import Counter

def get_data(input_file):
    """
    Reads the input file and returns the grid as a list of strings.

    Args:
        input_file: An opened file object containing the grid.
    
    Returns:
        list: A list of strings representing the grid.
    """
    return [line.strip() for line in input_file]

def get_times(grid):
    """
    Computes the minimum times to reach each cell from the endpoint 'E' using BFS.

    Args:
        grid (list): The grid as a list of strings.
    
    Returns:
        list: A 2D list of minimum times to reach each cell from 'E'.
    """
    # Find the endpoint 'E'
    end = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "E")

    # Initialize times with None and set the endpoint time to 0
    times = [[None for _ in line] for line in grid]
    times[end[0]][end[1]] = 0

    # BFS to calculate times
    time = 0
    to_visit = [end]
    while to_visit:
        time += 1
        next_visit = []
        for row, col in to_visit:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Directions: right, down, left, up
                new_row, new_col = row + dr, col + dc
                if times[new_row][new_col] is None and grid[new_row][new_col] != "#":
                    times[new_row][new_col] = time
                    next_visit.append((new_row, new_col))
        to_visit = next_visit

    return times

def count_cheats(grid, max_cheat_time):
    """
    Counts all possible cheats and their savings in time.

    Args:
        grid (list): The grid as a list of strings.
        max_cheat_time (int): Maximum time a cheat can save.
    
    Returns:
        Counter: A dictionary-like object counting occurrences of each cheat time savings.
    """
    m, n = len(grid), len(grid[0])
    times = get_times(grid)

    # Precompute all possible cheat directions and their times
    cheats_directions = {(dr, dc): dr + dc for dr in range(max_cheat_time + 1) for dc in range(max_cheat_time + 1 - dr)}
    cheats_directions |= {(dr, -dc): time for (dr, dc), time in cheats_directions.items()}
    cheats_directions |= {(-dr, dc): time for (dr, dc), time in cheats_directions.items()}

    # Find the starting point 'S'
    start = next((row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == "S")
    cheats = Counter()

    # Track visited cells
    visited = [[cell == "#" for cell in line] for line in grid]
    visited[start[0]][start[1]] = True

    # BFS to explore the grid
    time = 0
    to_visit = [start]
    total_time = times[start[0]][start[1]]
    while to_visit:
        next_visit = []
        for row, col in to_visit:
            # Evaluate cheats
            for (dr, dc), cheat_time in cheats_directions.items():
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and (time_ := times[new_row][new_col]) is not None
                    and (new_time := time + cheat_time + time_) < total_time
                ):
                    cheats[total_time - new_time] += 1
            # Continue traversing the grid
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if not visited[new_row][new_col] and grid[new_row][new_col] != "#":
                    visited[new_row][new_col] = True
                    next_visit.append((new_row, new_col))
        time += 1
        to_visit = next_visit

    return cheats

def part_1(grid, max_cheat_time=2, minimal_cheat=100):
    """
    Solves Part 1 of the puzzle by counting cheats with savings >= minimal_cheat.

    Args:
        grid (list): The grid as a list of strings.
        max_cheat_time (int): Maximum time a cheat can save.
        minimal_cheat (int): Minimum cheat saving to be considered.
    
    Returns:
        int: The number of cheats with time savings >= minimal_cheat.
    """
    cheats = count_cheats(grid, max_cheat_time)
    return sum(count for time, count in cheats.items() if time >= minimal_cheat)

def main():
    """
    Main function to run Part 1 of the puzzle.
    """
    with open('input.txt') as input_file:  # Open the input file
        grid = get_data(input_file)
    
    result = part_1(grid)
    print(f"Part 1 Result: {result}")

if __name__ == "__main__":
    main()
