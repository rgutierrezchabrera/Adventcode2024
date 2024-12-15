def parse_input(data):
    """Parses the input data into a list of robot positions and velocities."""
    robots = []
    for line in data.strip().split("\n"):
        pos, vel = line.split(" ")
        px, py = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robots(robots, width, height, seconds):
    """Simulates the robots' movement for the given number of seconds."""
    positions = []
    for (px, py), (vx, vy) in robots:
        nx = (px + vx * seconds) % width
        ny = (py + vy * seconds) % height
        positions.append((nx, ny))
    return positions

def count_quadrants(positions, width, height):
    """Counts the number of robots in each quadrant."""
    mid_x = width // 2
    mid_y = height // 2

    quadrants = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  # Ignore robots on the middle lines

        if x > mid_x and y < mid_y:
            quadrants[0] += 1  # Q1
        elif x < mid_x and y < mid_y:
            quadrants[1] += 1  # Q2
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1  # Q3
        elif x > mid_x and y > mid_y:
            quadrants[3] += 1  # Q4

    return quadrants

def compute_safety_factor(quadrants):
    """Computes the safety factor as the product of quadrant counts."""
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

def process_input(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return parse_input(data)

# Example test
example_data = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
example_robots = parse_input(example_data)
example_positions = simulate_robots(example_robots, width=11, height=7, seconds=100)
example_quadrants = count_quadrants(example_positions, width=11, height=7)
example_factor = compute_safety_factor(example_quadrants)
print("Example Quadrants:", example_quadrants)
print("Example Safety Factor:", example_factor)
assert example_factor == 12, "Test failed: example does not match!"
print("Test works.")

# Process input.txt
input_robots = process_input("input.txt")
input_positions = simulate_robots(input_robots, width=101, height=103, seconds=100)
input_quadrants = count_quadrants(input_positions, width=101, height=103)
input_factor = compute_safety_factor(input_quadrants)
print("Input Quadrants:", input_quadrants)
print("Input Safety Factor:", input_factor)