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
            expanded.extend([file_id] * size)  # Fill with file ID as integer
            file_id += 1
        else:
            expanded.extend(['.'] * size)  # Fill with free space
    return expanded


def compact_disk_whole_files(disk):
    """Compacts the disk by moving whole files to the leftmost free span that can fit them."""
    disk = disk.copy()  # Work with a copy of the disk to not modify the original
    length = len(disk)
    files_moved = set()  # Set to track which files have been moved

    # Start from the highest file ID and move towards the left
    file_ids = sorted(set(disk) - {'.'}, reverse=True)  # Get file IDs in descending order

    # Iterate over files from highest to lowest
    for file_id in file_ids:
        if file_id not in files_moved:  # Only attempt to move files that haven't been moved
            # Find all blocks of this file
            file_blocks = [k for k in range(length) if disk[k] == file_id]
            file_size = len(file_blocks)

            gap_found = False
            # Try to fit the file into a gap to its left
            for start in range(file_blocks[0]):  # Only consider gaps left of the file's current position
                if disk[start] == '.':  # Found the start of a free gap
                    gap_start = start
                    gap_end = start
                    while gap_end < length and disk[gap_end] == '.':
                        gap_end += 1
                    gap_size = gap_end - gap_start

                    # Debugging: Show gap details
                    #print(f"Gap found from index {gap_start} to {gap_end} (size {gap_size})")

                    # If the gap is large enough, move the file
                    if gap_size >= file_size:
                        # Debugging: Show the file that will be moved
                        #print(f"Moving file {file_id} (size {file_size}) into gap at {gap_start} to {gap_start + file_size - 1}")
                        
                        # Move the file into the gap
                        for k in range(file_size):
                            disk[gap_start + k] = file_id
                        # Clear the original file blocks
                        for k in file_blocks:
                            disk[k] = '.'

                        # Mark the file as moved
                        files_moved.add(file_id)
                        gap_found = True
                        break  # Move on to the next file after successfully moving this one

            # If no gap was found, we skip this file and move on
            #if not gap_found:
            #    print(f"File {file_id} couldn't be moved. Skipping.")

        # Debugging: Show the state of the disk after attempting to move a file
        #print("Current disk state:", ''.join(str(x) if x != '.' else '.' for x in disk))

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

#print("Expanded Disk:", ''.join(str(x) for x in expanded_disk))

compacted_disk = compact_disk_whole_files(expanded_disk)
#print("Compacted Disk:", ''.join(str(x) for x in compacted_disk))

checksum = calculate_checksum(compacted_disk)
print("Filesystem Checksum:", checksum)
