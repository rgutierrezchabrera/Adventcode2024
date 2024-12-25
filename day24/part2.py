# Open the input file and parse its content
with open("input.txt", "r") as file:
    # Skip the first section (initial wire values), stopping at the blank line
    for line in file:
        if line.isspace():
            break

    # Parse the gate formulas into a dictionary
    formulas = {}
    for line in file:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

# Helper function to construct wire names (e.g., x00, y03, z14)
def make_wire(char, num):
    return f"{char}{num:02d}"

# Verify if a 'z' wire is correct for a given bit position
def verify_z(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    if num == 0:  # Base case: z00 depends directly on x00 XOR y00
        return sorted([x, y]) == ["x00", "y00"]
    # Recursive case: z depends on XOR of intermediate XOR and carry bit
    return (
        verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or
        verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
    )

# Verify intermediate XOR operations
def verify_intermediate_xor(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

# Verify carry bit operations
def verify_carry_bit(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if num == 1:  # Base case: carry depends on x00 AND y00
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR":  # Recursive case: carry is based on carry propagation
        return False
    return (
        verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or
        verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)
    )

# Verify direct carry operations
def verify_direct_carry(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

# Verify recarry operations
def verify_recarry(wire, num):
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return (
        verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or
        verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
    )

# Verify if all 'z' wires are correct up to a given bit position
def verify(num):
    return verify_z(make_wire("z", num), num)

# Determine the current progress of correct 'z' wires
def progress():
    i = 0
    while True:
        if not verify(i):
            break
        i += 1
    return i

# List to store swapped wires
swaps = []

# Find the four pairs of swapped wires
for _ in range(4):
    baseline = progress()  # Check initial correctness of 'z' wires
    for x in formulas:
        for y in formulas:
            if x == y:
                continue
            # Try swapping x and y
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:  # Keep the swap if it improves correctness
                break
            # Undo the swap if it doesn't improve correctness
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    swaps += [x, y]  # Record the swapped wires

# Output the swapped wires as a sorted, comma-separated string
print(",".join(sorted(swaps)))
