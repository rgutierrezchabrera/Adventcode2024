def parse_input(input_str):
    """Parse the input string into the warehouse layout and the movement sequence."""
    lines = input_str.strip().split('\n')

    # Split the input into warehouse and moves based on the first line starting with '<' or '>'
    for i, line in enumerate(lines):
        if line.startswith('<') or line.startswith('>'):
            warehouse = lines[:i]
            moves = ''.join(lines[i:]).strip()
            return warehouse, moves

    # If no movement line is found, assume the last line contains the moves
    warehouse = lines[:-1]
    moves = lines[-1].strip()
    return warehouse, moves


def print_warehouse(warehouse):
    """Print the warehouse layout row by row (useful for debugging)."""
    for row in warehouse:
        print(row)
    print()


def move_robot(warehouse, moves):
    """Move the robot according to the moves sequence."""
    height, width = len(warehouse), len(warehouse[0])
    warehouse = [list(row) for row in warehouse]  # Convert to mutable list of lists

    # Find the initial position of the robot (@)
    robot_pos = None
    for y in range(height):
        for x in range(width):
            if warehouse[y][x] == '@':
                robot_pos = (x, y)
                break
        if robot_pos:
            break

    # Define the movement directions for the robot
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

    # Process each move in the sequence
    for move in moves:
        dx, dy = directions[move]
        new_x, new_y = robot_pos[0] + dx, robot_pos[1] + dy

        # Check if the new position is within bounds
        if 0 <= new_x < width and 0 <= new_y < height:
            # If the new position is empty, move the robot
            if warehouse[new_y][new_x] == '.':
                warehouse[robot_pos[1]][robot_pos[0]] = '.'  # Empty the current position
                warehouse[new_y][new_x] = '@'  # Place the robot at the new position
                robot_pos = (new_x, new_y)
            # If the new position contains a box, try to push it
            elif warehouse[new_y][new_x] == 'O':
                # Find the next available space to push the box
                next_x, next_y = new_x + dx, new_y + dy
                while 0 <= next_x < width and 0 <= next_y < height and warehouse[next_y][next_x] == 'O':
                    next_x, next_y = next_x + dx, next_y + dy
                if 0 <= next_x < width and 0 <= next_y < height and warehouse[next_y][next_x] == '.':
                    # Push the box to the new position and move the robot
                    warehouse[next_y][next_x] = 'O'
                    while (next_x, next_y) != (new_x, new_y):
                        prev_x, prev_y = next_x - dx, next_y - dy
                        warehouse[next_y][next_x] = warehouse[prev_y][prev_x]
                        next_x, next_y = prev_x, prev_y
                    warehouse[new_y][new_x] = '@'  # Move the robot to the box's original position
                    warehouse[robot_pos[1]][robot_pos[0]] = '.'  # Empty the robot's previous position
                    robot_pos = (new_x, new_y)

        # Optional: Print the warehouse after each move for debugging
        # print_warehouse([''.join(row) for row in warehouse])

    return [''.join(row) for row in warehouse]  # Return the final warehouse as a list of strings


def calculate_gps_sum(warehouse):
    """Calculate the GPS sum for all boxes ('O') in the warehouse."""
    gps_sum = 0
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == 'O':
                gps = x + (y * 100)  # GPS formula: x + (y * 100)
                gps_sum += gps
    return gps_sum


def solve_warehouse_woes(input_str):
    """Solve the warehouse puzzle: Parse input, process moves, and calculate the GPS sum."""
    warehouse, moves = parse_input(input_str)  # Parse the input
    final_warehouse = move_robot(warehouse, moves)  # Execute the robot's moves
    return calculate_gps_sum(final_warehouse)  # Calculate and return the GPS sum


# Test examples
example_input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
<^^>>>vv<v>>v<<"""

example_input2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########
<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# Solve the examples
example_result = solve_warehouse_woes(example_input)
print(f"Example 1 result: {example_result}")

example_result2 = solve_warehouse_woes(example_input2)
print(f"Example 2 result: {example_result2}")

# Reading from an input file and solving
with open('input.txt', 'r') as file:
    input_data = file.read()
result = solve_warehouse_woes(input_data)
print(f"Answer to Part one (input.txt): {result}")
