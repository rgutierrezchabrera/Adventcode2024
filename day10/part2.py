from collections import deque

# Function to perform DFS and count the distinct hiking trails from a trailhead
def count_trails(map_data, start_row, start_col):
    rows, cols = len(map_data), len(map_data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    trails = 0

    # DFS stack to explore the paths
    stack = [(start_row, start_col, [(start_row, start_col)])]  # (current_row, current_col, path)
    
    while stack:
        row, col, path = stack.pop()
        current_height = map_data[row][col]
        
        # If we reached a 9, count the trail
        if current_height == 9:
            trails += 1
            continue
        
        # Explore the 4 adjacent cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Ensure the new position is within bounds and hasn't been visited in the current path
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_height = map_data[new_row][new_col]
                
                # The next height must be exactly 1 greater than the current height
                if new_height == current_height + 1 and (new_row, new_col) not in path:
                    new_path = path + [(new_row, new_col)]
                    stack.append((new_row, new_col, new_path))
    
    return trails

# Main function to process the map and calculate the sum of ratings
def calculate_ratings(map_data):
    rows, cols = len(map_data), len(map_data[0])
    total_rating = 0
    
    # Iterate through all positions to find trailheads (height 0)
    for row in range(rows):
        for col in range(cols):
            if map_data[row][col] == 0:
                # Start DFS from the trailhead and compute its rating
                total_rating += count_trails(map_data, row, col)
    
    return total_rating

# Function to read the input from the file and convert it into a 2D list
def read_input(file_path):
    with open(file_path, 'r') as file:
        # Read the lines and convert each line into a list of integers
        map_data = [list(map(int, line.strip())) for line in file]
    return map_data

# Main execution flow
if __name__ == "__main__":
    # Read the map data from input.txt
    map_data = read_input('input.txt')
    
    # Calculate the sum of ratings for all trailheads
    result = calculate_ratings(map_data)
    
    # Output the result
    print(result)
