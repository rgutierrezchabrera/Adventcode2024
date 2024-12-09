import re

def process_memory(memory):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
    for match in re.finditer(pattern, memory):
        x, y = map(int, match.groups())
        total += x * y
    return total

# Read the input from the file
try:
    with open('input.txt', 'r') as file:
        corrupted_memory = file.read()
except FileNotFoundError:
    print("Error: 'input.txt' file not found.")
    exit(1)
except IOError:
    print("Error: Unable to read 'input.txt' file.")
    exit(1)

# Process the corrupted memory and calculate the result
result = process_memory(corrupted_memory)

# Print the result
print(f"Sum of multiplication results: {result}")