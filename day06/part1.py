def count_guard_positions(map_input):
    from collections import deque

    # Parse the input map
    grid = [list(line) for line in map_input.splitlines()]
    rows, cols = len(grid), len(grid[0])
    directions = deque(['^', '>', 'v', '<'])  # deque to handle right-turn logic
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}  # movement deltas

    # Locate the starting position and initial direction
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = '.'  # Clear initial direction from the map
                break
        if guard_pos:
            break

    # Ensure we have found the guard's starting position
    if guard_pos is None or guard_dir is None:
        raise ValueError("Guard's starting position not found in the map.")

    # Print the initial position and direction
    print(f"Guard's starting position: {guard_pos}, Facing: {guard_dir}")

    # Track distinct visited positions
    visited_positions = set()
    visited_positions.add(guard_pos)

    # Simulate the guard's movement
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
            visited_positions.add(guard_pos)

    return len(visited_positions)


# Read the input from the file
with open("input.txt", "r") as file:
    map_input = file.read()

# Calculate the result
result = count_guard_positions(map_input)

# Output the number of distinct positions visited
print(f"Distinct positions visited by the guard: {result}")
