# Open the input file and parse its content
with open("input.txt", "r") as file:
    lines = file.readlines()

# Dictionary to store known wire values
known = {}

# Parse the initial wire values from the first section of the input
for line in lines:
    if line.isspace():  # Stop when an empty line is encountered
        break
    wire, value = line.split(": ")  # Split each line into wire name and value
    known[wire] = int(value)  # Store the wire's value in the known dictionary

# Dictionary to store gate formulas and connections
formulas = {}

# Parse the gate operations and output connections from the second section of the input
for line in lines[len(known) + 1:]:
    input1, operation, input2, output = line.replace(" -> ", " ").split()
    formulas[output] = (operation, input1, input2)

# Define supported gate operations as lambda functions
operators = {
    "OR": lambda x, y: x | y,    # Bitwise OR
    "AND": lambda x, y: x & y,  # Bitwise AND
    "XOR": lambda x, y: x ^ y   # Bitwise XOR
}

# Recursive function to calculate the value of a wire
def calc(wire):
    if wire in known:  # Return the value if already known
        return known[wire]
    operation, input1, input2 = formulas[wire]  # Retrieve operation and inputs
    known[wire] = operators[operation](calc(input1), calc(input2))  # Compute value
    return known[wire]

# List to store the values of the 'z' wires (outputs)
z = []
i = 0

# Iterate through all 'z' wires in sequence
while True:
    key = f"z{i:02d}"  # Generate the wire name (e.g., z00, z01, ...)
    if key not in formulas:  # Stop if the wire does not exist in formulas
        break
    z.append(calc(key))  # Calculate and store the value
    i += 1

# Combine the binary values of 'z' wires into a single decimal number
result = int("".join(map(str, z[::-1])), 2)

# Output the final result
print(result)
