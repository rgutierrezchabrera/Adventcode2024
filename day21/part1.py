import sys
from functools import cache
from itertools import permutations

def read_input(file_path='input.txt'):
    """Read the input file and return a list of codes."""
    with open(file_path) as f:
        return f.read().splitlines()

# Define the layout of the numeric keypad
NUMERIC_KEYPAD = [
    '789',
    '456',
    '123',
    ' 0A'
]
# Create a dictionary mapping each key to its (x, y) coordinates
NUMERIC_KEYPAD = {key: (x, y) for y, line in enumerate(NUMERIC_KEYPAD) for x, key in enumerate(line) if key != ' '}

# Define the layout of the directional keypad
DIRECTIONAL_KEYPAD = [
    ' ^A',
    '<v>'
]
# Create a dictionary mapping each key to its (x, y) coordinates
DIRECTIONAL_KEYPAD = {key: (x, y) for y, line in enumerate(DIRECTIONAL_KEYPAD) for x, key in enumerate(line) if key != ' '}

# Define the directions and their corresponding coordinate changes
DIRECTIONS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

@cache
def get_presses(sequence, depth=2, is_directional=False, current=None):
    """
    Recursively calculate the minimum number of button presses needed to type the sequence.
    
    :param sequence: The sequence of buttons to press
    :param depth: The depth of recursion (number of robots in the chain)
    :param is_directional: Whether we're using the directional keypad
    :param current: The current position on the keypad
    :return: The minimum number of button presses
    """
    keypad = DIRECTIONAL_KEYPAD if is_directional else NUMERIC_KEYPAD
    if not sequence:
        return 0
    if not current:
        current = keypad['A']

    cx, cy = current
    px, py = keypad[sequence[0]]
    dx, dy = px - cx, py - cy

    # Generate the sequence of directional buttons to press
    buttons = '>' * max(0, dx) + '<' * max(0, -dx) + 'v' * max(0, dy) + '^' * max(0, -dy)

    if depth:
        perm_lens = []
        for perm in set(permutations(buttons)):
            cx, cy = current
            for button in perm:
                dx, dy = DIRECTIONS[button]
                cx += dx
                cy += dy
                if (cx, cy) not in keypad.values():
                    break
            else:
                perm_lens.append(get_presses(perm + ('A',), depth - 1, True))
        min_len = min(perm_lens) if perm_lens else len(buttons) + 1
    else:
        min_len = len(buttons) + 1
    return min_len + get_presses(sequence[1:], depth, is_directional, (px, py))

def calculate_part1(codes):
    """Calculate the sum of complexities for all codes."""
    return sum(int(code[:-1]) * get_presses(code) for code in codes)

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    codes = read_input(input_file)
    result = calculate_part1(codes)
    print(result)
