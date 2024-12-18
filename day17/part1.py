import re

# Parse input: Extract registers A, B, C and the program from input
a, b, c, *program = map(int, re.findall(r"\d+", open(0).read()))

# Initialize the instruction pointer and output list
pointer = 0
output = []

def combo(operand):
    """
    Determine the value of the operand based on its type.
    - If 0 <= operand <= 3, it's a literal value.
    - If operand == 4, it represents the value in register A.
    - If operand == 5, it represents the value in register B.
    - If operand == 6, it represents the value in register C.
    """
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    else:
        raise RuntimeError("Unrecognized combo operand", operand)

# Execute the program
while pointer < len(program):
    # Fetch the current instruction and its operand
    ins = program[pointer]
    operand = program[pointer + 1]

    # Process instructions based on their opcode
    if ins == 0:  # adv: Perform division and update register A
        a = a >> combo(operand)
    elif ins == 1:  # bxl: XOR register B with the literal operand
        b = b ^ operand
    elif ins == 2:  # bst: Modulo combo operand by 8 and update register B
        b = combo(operand) % 8
    elif ins == 3:  # jnz: Jump to literal operand if register A is not zero
        if a != 0:
            pointer = operand
            continue
    elif ins == 4:  # bxc: XOR register B with register C
        b = b ^ c
    elif ins == 5:  # out: Output (combo operand % 8)
        output.append(combo(operand) % 8)
    elif ins == 6:  # bdv: Perform division and update register B
        b = a >> combo(operand)
    elif ins == 7:  # cdv: Perform division and update register C
        c = a >> combo(operand)
    else:
        raise RuntimeError("Unrecognized instruction", ins)

    # Move the instruction pointer to the next instruction
    pointer += 2

# Print the output values, joined by commas
print(*output, sep=",")
