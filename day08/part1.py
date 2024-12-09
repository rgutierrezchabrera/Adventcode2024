def find_antinodes(map_str):
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
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i+1:]:
                antinode1 = (2*x1 - x2, 2*y1 - y2)
                antinode2 = (2*x2 - x1, 2*y2 - y1)
                
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)
    
    return len(antinodes)

# Read input from file
with open('input.txt', 'r') as file:
    map_str = file.read()

result = find_antinodes(map_str)
print(f"Number of unique antinode locations: {result}")