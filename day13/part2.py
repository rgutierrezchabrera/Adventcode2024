import sys
import pyperclip as pc
from collections import defaultdict, Counter, deque
import numpy as np
import time

# Function to print and copy to clipboard
def pr(output):
    print(output)
    pc.copy(output)

# Increase recursion limit for deep recursion in the solver
sys.setrecursionlimit(10**6)

# Direction vectors for grid movement (not directly used here)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

# Input file handling
input_file = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
total_score = 0  # Variable to accumulate scores for all machines
machines_solved = 0  # Counter for machines where the prize is achievable
data = open(input_file).read().strip()

# Cost constants for buttons
COST_BUTTON_A = 3
COST_BUTTON_B = 1
P2_CONSTANT = 10**13  # Large constant to handle "infinite" cycles

# Function to solve the prize problem for a single machine
def solve(ax, ay, bx, by, px, py):
    best_solution = None  # Tracks the best solution (minimum score)

    # Brute force over t1 (Button A presses) and t2 (Button B presses)
    for t1 in range(600):
        for t2 in range(600):
            cost = COST_BUTTON_A * t1 + COST_BUTTON_B * t2
            dx = ax * t1 + bx * t2
            dy = ay * t1 + by * t2

            # Check if X and Y coordinates align and are positive
            if dx == dy and dx > 0:
                score = dx / cost
                if best_solution is None or score < best_solution[0]:
                    best_solution = (score, t1, t2, cost, dx)

    # If no solution was found, return 0
    if best_solution is None:
        return 0

    # Extract best solution values
    _, t1, t2, cost, dx = best_solution
    large_amount = (P2_CONSTANT - 40000) // dx

    # Recursive function for dynamic programming
    memo = {}

    def recursive_cost(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        if x == 0 and y == 0:
            return 0
        if x < 0 or y < 0:
            return float('inf')  # Return a very large number if out of bounds

        # Compute cost for each button press
        cost_a = COST_BUTTON_A + recursive_cost(x - ax, y - ay)
        cost_b = COST_BUTTON_B + recursive_cost(x - bx, y - by)

        # Memoize and return the minimum cost
        result = min(cost_a, cost_b)
        memo[(x, y)] = result
        return result

    # Calculate the remaining cost after adjusting for large cycles
    remaining_cost = recursive_cost(px + P2_CONSTANT - large_amount * dx, py + P2_CONSTANT - large_amount * dx)

    # If the remaining cost is feasible, return the total cost; otherwise, return 0
    if remaining_cost < 10**15:
        return remaining_cost + large_amount * cost
    else:
        return 0

# Split input data into machine definitions and process each
machines = data.split('\n\n')  # Machines are separated by blank lines

# Start the timer
start_time = time.time()

for machine_index, machine_data in enumerate(machines):
    # Extract lines for Button A, Button B, and Prize
    button_a, button_b, prize = machine_data.split('\n')

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

    # Solve for the score of achieving the prize for this machine
    score = solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)

    # If the score is greater than 0, it means the prize is achievable
    if score > 0:
        machines_solved += 1

    # Accumulate the total score
    total_score += score

    # Debug output for the current machine
    #print(machine_index, len(machines), prize, total_score, machines_solved)

# Output the total score
print("--- Part Two ---")
print("Answer: " + str(total_score))

# Stop the timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")