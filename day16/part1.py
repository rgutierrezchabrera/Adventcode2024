import heapq

# Convert maze input to a 2D list
def parse_maze(maze_str):
    return [list(row) for row in maze_str.strip().split('\n')]

# Find start and end points in the maze
def find_start_end(maze):
    start, end = None, None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end

# Get all valid neighboring cells and their directions
def get_neighbors(x, y, direction):
    return [
        ((x+1, y), 0, 'E'), ((x-1, y), 0, 'W'),
        ((x, y+1), 0, 'S'), ((x, y-1), 0, 'N')
    ]

# Calculate the cost of rotating from one direction to another
def rotate_cost(current_dir, new_dir):
    dirs = 'NESW'
    return min((dirs.index(new_dir) - dirs.index(current_dir)) % 4,
               (dirs.index(current_dir) - dirs.index(new_dir)) % 4) * 1000

# Solve the maze using a priority queue for the BFS
def solve_maze(maze):
    start, end = find_start_end(maze)
    queue = [(0, start[0], start[1], 'E')]  # Starting direction is 'E' (East)
    visited = set()  # To avoid revisiting the same state

    while queue:
        score, x, y, direction = heapq.heappop(queue)  # Pop the lowest-cost option
        
        if (x, y) == end:  # If the end is reached, return the score
            return score
        
        if (x, y, direction) in visited:  # Skip already visited states
            continue
        visited.add((x, y, direction))
        
        for (nx, ny), move_cost, new_dir in get_neighbors(x, y, direction):
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != '#':
                new_score = score + move_cost + 1 + rotate_cost(direction, new_dir)  # Update the score
                heapq.heappush(queue, (new_score, nx, ny, new_dir))  # Push the new state onto the queue
    
    return float('inf')  # If no path is found

# Example maze (as a string)
example_maze = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

# Solve example maze
example_result = solve_maze(parse_maze(example_maze))
print(f"Example maze result: {example_result}")

# Test the solution for input.txt
with open('input.txt', 'r') as f:
    input_maze = f.read()
input_result = solve_maze(parse_maze(input_maze))
print(f"Answer to Part One (input.txt): {input_result}")
