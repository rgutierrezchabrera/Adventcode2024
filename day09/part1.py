def parse_disk_map(disk_map):
    """Parses the disk map into a list of tuples representing files and free spaces."""
    disk = []
    for i, char in enumerate(disk_map):
        size = int(char)
        if i % 2 == 0:
            disk.append(('file', size))  # Even index: file
        else:
            disk.append(('free', size))  # Odd index: free space
    return disk


def expand_disk_map(disk):
    """Expands the compact disk representation into a full layout."""
    expanded = []
    file_id = 0
    for kind, size in disk:
        if kind == 'file':
            expanded.extend([file_id] * size)  # Fill with file ID
            file_id += 1
        else:
            expanded.extend(['.'] * size)  # Fill with free space
    return expanded


def compact_disk(disk):
    """Compacts the disk by moving file blocks to the leftmost free spaces."""
    disk = disk.copy()  # Work on a copy to avoid modifying the original
    length = len(disk)
    right_pointer = length - 1

    for left_pointer in range(length):
        if disk[left_pointer] == '.':  # Found a free space
            # Find the rightmost non-free block
            while right_pointer > left_pointer and disk[right_pointer] == '.':
                right_pointer -= 1
            
            if right_pointer > left_pointer:
                # Swap the free space with the non-free block
                disk[left_pointer], disk[right_pointer] = disk[right_pointer], disk[left_pointer]
            else:
                # All blocks to the right are free spaces, we're done
                break

    return disk



def calculate_checksum(disk):
    """Calculates the filesystem checksum."""
    checksum = 0
    for pos, file_id in enumerate(disk):
        if file_id != '.':  # Skip free spaces
            checksum += pos * int(file_id)  # Ensure file_id is treated as an integer
    return checksum


# Read input data from input.txt
with open('input.txt', 'r') as file:
    input_data = file.read().strip()

# Process the input data
parsed_disk = parse_disk_map(input_data)
expanded_disk = expand_disk_map(parsed_disk)

print("Expanded Disk:", ''.join(str(x) for x in expanded_disk))

compacted_disk = compact_disk(expanded_disk)
#print("Compacted Disk:", ''.join(str(x) for x in compacted_disk))

checksum = calculate_checksum(compacted_disk)
print("Filesystem Checksum:", checksum)
