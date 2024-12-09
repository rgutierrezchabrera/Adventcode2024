def is_x_mas(grid, row, col):
    # Ensure the grid window is valid for a 3x3 check
    if row + 2 >= len(grid) or col + 2 >= len(grid[0]):
        return 0
    
    # Extract characters in the diagonals of the 3x3 subgrid
    top_left_diag = [grid[row][col], grid[row+1][col+1], grid[row+2][col+2]]
    bottom_left_diag = [grid[row+2][col], grid[row+1][col+1], grid[row][col+2]]
    
    # Check for "MAS" in either direction
    mas = ['M', 'A', 'S']
    if (top_left_diag == mas or top_left_diag == mas[::-1]) and \
       (bottom_left_diag == mas or bottom_left_diag == mas[::-1]):
        return 1
    return 0

def count_x_mas(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += is_x_mas(grid, i, j)
    return total

# Read the input from file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file if line.strip()]

# Count X-MAS occurrences
result = count_x_mas(grid)
print(f"X-MAS appears {result} times in the word search.")
