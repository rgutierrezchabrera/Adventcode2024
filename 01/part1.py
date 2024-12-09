def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Initialize total distance
    total_distance = 0
    
    # Calculate the total distance
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

def read_input_and_calculate_distance(filename):
    left_list = []
    right_list = []
    
    # Open the file and read its contents
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers and append them to the lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Calculate and return the total distance
    return calculate_total_distance(left_list, right_list)

# Call the function with the input file
filename = 'input.txt'
result = read_input_and_calculate_distance(filename)

# Output the result
print(result)
