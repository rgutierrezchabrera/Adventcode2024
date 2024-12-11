from collections import deque

# Function to perform BFS and count the reachable 9's from a trailhead
def bfs(map_data, start_row, start_col):
    rows, cols = len(map_data), len(map_data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])
    reachable_nines = 0

    while queue:
        row, col = queue.popleft()
        current_height = map_data[row][col]
        
        # If we reached a 9, count it
        if current_height == 9:
            reachable_nines += 1
        
        # Explore the 4 adjacent cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Ensure the new position is within bounds and hasn't been visited
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                new_height = map_data[new_row][new_col]
                
                # The next height must be exactly 1 greater than the current height
                if new_height == current_height + 1:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
    
    return reachable_nines

# Main function to process the map and calculate the sum of scores
def calculate_scores(map_data):
    rows, cols = len(map_data), len(map_data[0])
    total_score = 0
    
    # Iterate through all positions to find trailheads (height 0)
    for row in range(rows):
        for col in range(cols):
            if map_data[row][col] == 0:
                # Start BFS from the trailhead and compute the score
                total_score += bfs(map_data, row, col)
    
    return total_score

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
    
    # Calculate the sum of scores for all trailheads
    result = calculate_scores(map_data)
    
    # Output the result
    print(result)
