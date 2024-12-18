import sys
import re

# Input Parsing
# The input provided from standard input looks like this:
# Register A: 60589763
# Register B: 0
# Register C: 0
#
# Program: 2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0

# Read input data from standard input
input_data = sys.stdin.read().strip()

# Split the input into parts based on the empty line
registers_data, program_data = input_data.split("\n\n")

# Extract the values for registers (only A is needed for this task)
initial_registers = [int(num) for num in re.findall(r'\d+', registers_data)]  # A, B, C
# Extract the program as a list of integers
program = list(map(int, re.findall(r'\d+', program_data)))

# Recursive function to find the correct initial value of A
def find_initial_a(program, current_value):
    """
    Recursively find the smallest value for A such that the program outputs itself.
    :param program: List[int] - The program sequence to match.
    :param current_value: int - The current candidate for A's initial value.
    :return: int - The smallest valid initial value of A or None if not found.
    """
    # Base case: If program is empty, return the current candidate for A
    if not program:
        return current_value
    
    # Iterate through possible values for the least significant 3 bits
    for t in range(8):
        # Calculate candidate for A by setting its least significant 3 bits to t
        a = (current_value << 3) | t

        # Simulate the program based on its translated logic
        # Program: 2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0
        b = a % 8               # Program: 2,4  -> b = a % 8
        b = b ^ 5               # Program: 1,5  -> b = b ^ 5
        c = a >> b              # Program: 7,5  -> c = a >> b
        b = b ^ 6               # Program: 1,6  -> b = b ^ 6
        b = b ^ c               # Program: 4,1  -> b = b ^ c

        # Check if the output matches the last value in the program
        if b % 8 == program[-1]:
            # Recursive call with the rest of the program and the updated candidate
            result = find_initial_a(program[:-1], a)
            if result is not None:  # If a solution is found, return it
                return result

    # If no valid value is found, return None
    return None

# Run the recursive function with the given program and initial candidate of 0
result = find_initial_a(program, 0)

# Output the result
print("Smallest valid initial value of A:", result)
