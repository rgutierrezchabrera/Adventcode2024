def find_antinodes_part2(map_str):
    lines = map_str.strip().split('\n')
    height = len(lines)
    width = len(lines[0])
    
    antennas = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    
    antinodes = set()
    for freq, positions in antennas.items():
        if len(positions) > 1:
            antinodes.update(positions)  # Add antenna positions as antinodes
        
        for i, (x1, y1) in enumerate(positions):
            for j, (x2, y2) in enumerate(positions[i+1:], start=i+1):
                dx, dy = x2 - x1, y2 - y1
                
                # Check all points on the line between and beyond the antennas
                x, y = x1, y1
                while 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))
                    x += dx
                    y += dy
                
                # Check points in the opposite direction
                x, y = x1 - dx, y1 - dy
                while 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))
                    x -= dx
                    y -= dy

    return len(antinodes)

# Read input from file
with open('input.txt', 'r') as file:
    map_str = file.read()

result = find_antinodes_part2(map_str)
print(f"Number of unique antinode locations: {result}")