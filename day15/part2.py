import sys
import pyperclip

# Increase the recursion limit to handle larger grids if needed
sys.setrecursionlimit(1000000)

# Read input from the file
with open("input.txt") as file:
    input_data = file.read().strip()

# Function to print and copy output to clipboard for debugging or result sharing
def printc(text):
    pyperclip.copy(text)
    print(text)

# Initialize the answer and result variables
answer = 0

# Split the input into two parts: grid and move instructions
grid_data, moves_data = input_data.split("\n\n")

# Convert the grid input into a list of lists for easier manipulation
grid = [list(row) for row in grid_data.split("\n")]
grid_rows, grid_cols = len(grid), len(grid[0])  # Get the dimensions of the grid

# Create a new grid that is twice as wide and handles wider boxes
new_grid = []
for row in grid:
    new_row = []
    for cell in row:
        if cell == "#":
            new_row.append("#")  # Wall becomes double wide
            new_row.append("#")
        elif cell == "O":
            new_row.append("[")  # Box becomes wide represented as []
            new_row.append("]")
        elif cell == ".":
            new_row.append(".")  # Empty space becomes double wide
            new_row.append(".")
        elif cell == "@":
            new_row.append("@")  # Robot becomes wide represented as @.
            new_row.append(".")
    new_grid.append(new_row)

# Now new_grid represents the modified grid with twice the width
grid = new_grid
grid_rows, grid_cols = len(grid), len(grid[0])  # Update dimensions for the new grid

# Find the initial position of the robot (represented by '@')
current_x, current_y = 0, 0
for i in range(grid_rows):
    for j in range(grid_cols):
        if grid[i][j] == "@":
            current_x, current_y = i, j  # Set robot coordinates
            break

# Clean up and track the move instructions
move_instructions = moves_data.replace("\n", "")
print("Number of instructions:", len(move_instructions))

# Process each move in the sequence
for move_idx, move in enumerate(move_instructions):
    # Direction mapping for moves
    delta_x, delta_y = {
        "^": (-1, 0),  # Up
        "v": (1, 0),   # Down
        ">": (0, 1),   # Right
        "<": (0, -1)   # Left
    }[move]

    # List to keep track of coordinates to move
    coordinates_to_move = [(current_x, current_y)]  # Coordinates to move
    idx = 0
    move_impossible = False  # Flag to check if a move is impossible

    while idx < len(coordinates_to_move):
        x, y = coordinates_to_move[idx]
        new_x, new_y = x + delta_x, y + delta_y  # New coordinates

        # Check if the new position is a box
        if grid[new_x][new_y] in "O[]":
            if (new_x, new_y) not in coordinates_to_move:
                coordinates_to_move.append((new_x, new_y))
            if grid[new_x][new_y] == "[":  # Left side of the box
                if (new_x, new_y + 1) not in coordinates_to_move:
                    coordinates_to_move.append((new_x, new_y + 1))
            if grid[new_x][new_y] == "]":  # Right side of the box
                if (new_x, new_y - 1) not in coordinates_to_move:
                    coordinates_to_move.append((new_x, new_y - 1))
        # Stop if we hit a wall
        elif grid[new_x][new_y] == "#":
            move_impossible = True
            break
        idx += 1

    # If the move is impossible (i.e., blocked by a wall), continue to the next move
    if move_impossible:
        continue

    # Now move the elements in the grid (use a temporary grid to avoid simultaneous updates)
    temp_grid = [[grid[i][j] for j in range(grid_cols)] for i in range(grid_rows)]
    for x, y in coordinates_to_move:
        temp_grid[x][y] = "."  # Empty the old positions
    for x, y in coordinates_to_move:
        temp_grid[x + delta_x][y + delta_y] = grid[x][y]  # Move the elements to the new positions

    # Update the grid with the new configuration
    grid = temp_grid

    # Update the robot's current position
    current_x += delta_x
    current_y += delta_y

# Calculate the sum for all boxes (represented by '[' in the new grid)
# We only check for the left edges of the boxes '[', as this is the modified representation
for i in range(grid_rows):
    for j in range(grid_cols):
        if grid[i][j] != "[":
            continue
        answer += 100 * i + j  # GPS formula: x + (y * 100)

# Output the result
print("Answer to Part Two:", answer)
