import sys
import pyperclip as pc
from collections import defaultdict, Counter, deque
import time

# Function to print and copy to clipboard
def pr(output):
    print(output)
    pc.copy(output)

# Increase recursion limit to handle deep recursion in the solver
sys.setrecursionlimit(10**6)

# Direction vectors for grid movement (not used in this code but useful for general grid problems)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

# Input file handling
input_file = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
total_cost = 0  # Variable to store the total cost of achieving prizes
data = open(input_file).read().strip()  # Read and strip whitespace from input file

# Grid dimensions
grid_rows = len(data.split('\n'))
grid_cols = len(data.split('\n')[0])

# Cost constants
COST_BUTTON_A = 3
COST_BUTTON_B = 1

# Function to solve the minimum cost to achieve the prize coordinates
def solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y):
    # Memoization dictionary to store previously computed results
    memo = {}

    # Recursive helper function
    def calculate_cost(x, y):
        # Check if result is already cached
        if (x, y) in memo:
            return memo[(x, y)]

        # Base case: prize reached
        if x == 0 and y == 0:
            return 0

        # If coordinates are out of bounds, return an infeasible cost
        if x < 0 or y < 0:
            return float('inf')

        # Calculate the minimum cost using either Button A or Button B
        cost = min(
            COST_BUTTON_A + calculate_cost(x - button_a_x, y - button_a_y),
            COST_BUTTON_B + calculate_cost(x - button_b_x, y - button_b_y)
        )

        # Store the result in the memoization dictionary
        memo[(x, y)] = cost
        return cost

    # Compute the answer for the given prize coordinates
    result = calculate_cost(prize_x, prize_y)

    # If the cost exceeds a threshold, return 0 (prize not achievable)
    return result if result < 1000 else 0

# Parse input into machines and process each
machines = data.split('\n\n')  # Each machine block is separated by a blank line

# Start the timer
start_time = time.time()

for machine in machines:
    # Extract information about buttons and prize
    button_a, button_b, prize = machine.split('\n')

    # Parse Button A data
    button_a_parts = button_a.split()  # ['Button', 'A:', 'X+55,', 'Y+84']
    button_a_x = int(button_a_parts[2].split('+')[1].strip(','))  # Extract X value
    button_a_y = int(button_a_parts[3].split('+')[1].strip(','))  # Extract Y value

    # Parse Button B data
    button_b_parts = button_b.split()  # ['Button', 'B:', 'X+23,', 'Y+76']
    button_b_x = int(button_b_parts[2].split('+')[1].strip(','))  # Extract X value
    button_b_y = int(button_b_parts[3].split('+')[1].strip(','))  # Extract Y value

    # Parse Prize data
    prize_parts = prize.split()  # ['Prize:', 'X=6049,', 'Y=5045']
    prize_x = int(prize_parts[1].split('=')[1].strip(','))  # Extract X value
    prize_y = int(prize_parts[2].split('=')[1])            # Extract Y value

    # Solve for the cost to achieve the prize for this machine and accumulate the total
    total_cost += solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)

# Output the total cost
print("--- Part One ---")
print("Answer: " + str(total_cost))

# Stop the timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")