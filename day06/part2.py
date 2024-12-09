from collections import deque

# Function to simulate the guard's movement
def simulate_guard_movement(grid, guard_pos, guard_dir):
    rows, cols = len(grid), len(grid[0])
    directions = deque(['^', '>', 'v', '<'])  # Directions in order: Up, Right, Down, Left
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}  # Movement deltas

    visited_positions = set()  # Set to track visited positions along with direction

    # Start simulating the guard's movement
    while True:
        # Calculate the position in front of the guard
        dr, dc = moves[guard_dir]
        next_r, next_c = guard_pos[0] + dr, guard_pos[1] + dc

        # Check if out of bounds
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        # Check if there's an obstacle
        if grid[next_r][next_c] == '#':
            # Turn right (rotate the direction clockwise)
            directions.rotate(-1)  # Right turn
            guard_dir = directions[0]
        else:
            # Move forward
            guard_pos = (next_r, next_c)

            # Check if this position and direction has been visited before
            if (guard_pos, guard_dir) in visited_positions:
                return True  # A loop is detected

            # Otherwise, add the position and direction to the visited set
            visited_positions.add((guard_pos, guard_dir))

    return False  # No loop detected

# Function to count all positions where placing an obstacle results in a loop
def count_loop_inducing_obstacles(map_input):
    # Parse the map input into a grid
    grid = [list(line) for line in map_input.splitlines()]
    rows, cols = len(grid), len(grid[0])

    # Locate the starting position and direction of the guard
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['^', '>', 'v', '<']:  # Find the guard's starting direction
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = '.'  # Clear the initial direction from the map
                break
        if guard_pos:
            break

    # Ensure we found the guard's position and direction
    if guard_pos is None or guard_dir is None:
        raise ValueError("Guard's starting position not found in the map.")

    # Variable to count the number of loop-inducing obstacles
    total_loops = 0

    # Try placing an obstacle at every free position (i.e., '.') that is not the guard's starting position
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != guard_pos:
                # Temporarily add an obstacle and simulate the guard's movement
                grid[r][c] = '#'
                if simulate_guard_movement(grid, guard_pos, guard_dir):
                    total_loops += 1
                # Restore the grid to its original state
                grid[r][c] = '.'

    return total_loops

# Read the input from the file
with open("input.txt", "r") as file:
    map_input = file.read()

# Calculate the result
result = count_loop_inducing_obstacles(map_input)

# Output the number of loop-inducing positions
print(f"Number of positions where an obstacle creates a loop: {result}")
