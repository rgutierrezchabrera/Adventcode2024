import heapq
from collections import deque

# Read the grid from 'input.txt'
def read_grid(filename='input.txt'):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f]

# Find the start ('S') and end ('E') points in the grid
def find_start_end(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
            elif grid[r][c] == 'E':
                end_row, end_col = r, c
    return (start_row, start_col), (end_row, end_col)

# Calculate rotation cost between directions: clockwise or counterclockwise
def rotate_cost(current_dir, new_dir):
    dirs = 'NESW'
    return min((dirs.index(new_dir) - dirs.index(current_dir)) % 4,
               (dirs.index(current_dir) - dirs.index(new_dir)) % 4) * 1000

# Perform the BFS with a priority queue to find the best cost to each state
def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = start
    end_row, end_col = end
    dir_row, dir_col = 0, 1  # Starting direction: East
    start_cost = 0           # Starting cost
    best_cost = float('inf') # Best cost to reach the end
    end_states = set()

    pq = [(start_cost, start_row, start_col, dir_row, dir_col)]
    lowest_cost = {(start_row, start_col, dir_row, dir_col): 0}
    backtrack = {}  # Dictionary to backtrack to starting points

    while pq:
        cost, row, col, row_step, col_step = heapq.heappop(pq)
        
        if cost > lowest_cost.get((row, col, row_step, col_step), float('inf')):
            continue  # Skip if this is not the lowest cost to this state

        if grid[row][col] == 'E':  # If end is reached, update the best cost
            if cost > best_cost:
                break  # Exit early if we already found a worse path
            best_cost = cost
            end_states.add((row, col, row_step, col_step))

        # Try all possible moves: forward, rotate clockwise, rotate counterclockwise
        for new_cost, new_row, new_col, new_row_step, new_col_step in [
            (cost + 1, row + row_step, col + col_step, row_step, col_step),  # Move forward
            (cost + 1000, row, col, col_step, -row_step),  # Turn clockwise
            (cost + 1000, row, col, -col_step, row_step),  # Turn counterclockwise
        ]:
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
                lowest = lowest_cost.get((new_row, new_col, new_row_step, new_col_step), float('inf'))
                if new_cost > lowest:
                    continue  # Skip if this is not a cheaper path
                
                # Update the backtrack dictionary and lowest cost
                if new_cost < lowest:
                    backtrack[(new_row, new_col, new_row_step, new_col_step)] = set()
                    lowest_cost[(new_row, new_col, new_row_step, new_col_step)] = new_cost
                backtrack[(new_row, new_col, new_row_step, new_col_step)].add((row, col, row_step, col_step))
                heapq.heappush(pq, (new_cost, new_row, new_col, new_row_step, new_col_step))

    return backtrack, end_states, best_cost

# Backtrack to find all possible start points that can reach the end
def backtrack_to_start(backtrack, end_states):
    states = deque(end_states)
    seen = set(end_states)

    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):  # Backtrack to previous states
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    return seen

def main():
    grid = read_grid()  # Read the grid from input.txt
    start, end = find_start_end(grid)  # Find start and end positions
    backtrack, end_states, best_cost = bfs(grid, start, end)  # Perform BFS to find paths

    # Backtrack to find all valid starting positions
    seen = backtrack_to_start(backtrack, end_states)
    
    # Print the result: number of distinct starting positions that can reach the end
    print("Answer to Part Two (input.txt):", len({(row, col) for row, col, _, _ in seen}))

if __name__ == "__main__":
    main()
