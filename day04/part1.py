def search_xmas(grid, row, col):
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # horizontal and vertical
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonal
    ]
    count = 0
    for dx, dy in directions:
        if (0 <= row + 3*dx < len(grid) and 
            0 <= col + 3*dy < len(grid[0]) and
            grid[row][col] == 'X' and
            grid[row+dx][col+dy] == 'M' and
            grid[row+2*dx][col+2*dy] == 'A' and
            grid[row+3*dx][col+3*dy] == 'S'):
            count += 1
    return count

def count_xmas(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += search_xmas(grid, i, j)
    return total

# Read the input from file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file if line.strip()]

# Count XMAS occurrences
result = count_xmas(grid)
print(f"XMAS appears {result} times in the word search.")