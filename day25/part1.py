import sys

# Initialize lists to store lock and key schematics
locks = []
keys = []

# Read the input file (default: 'input.txt') and split into schematics
input_file = sys.argv[1] if len(sys.argv) > 1 else './input.txt'
with open(input_file) as f:
    schematics = f.read().split('\n\n')

# Process each schematic
for schematic in schematics:
    # Split schematic into lines
    rows = list(schematic.splitlines())
    
    # Determine if the schematic is a lock or a key
    if rows[0][0] == '#':  # Locks start with a filled top row
        # Calculate pin heights for the lock
        locks.append([
            sum(rows[y][x] == '#' for y in range(1, len(rows)))  # Count '#' from the second row onwards
            for x in range(len(rows[0]))  # Iterate over columns
        ])
    else:  # Keys start with an empty top row
        # Calculate key heights
        keys.append([
            sum(rows[y][x] == '#' for y in range(len(rows) - 1))  # Count '#' up to the second-last row
            for x in range(len(rows[0]))  # Iterate over columns
        ])

# Count compatible lock-key pairs
compatible_pairs = sum(
    all(k + l <= 5 for k, l in zip(key, lock))  # Check compatibility column by column
    for key in keys  # Iterate over all keys
    for lock in locks  # Iterate over all locks
)

# Print the result
print(f"Your puzzle answer is: {compatible_pairs}")
