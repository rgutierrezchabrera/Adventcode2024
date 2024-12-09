from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)
    
    # Initialize similarity score
    similarity_score = 0
    
    # Calculate the similarity score
    for number in left_list:
        similarity_score += number * right_counts[number]
    
    return similarity_score

def read_input_and_calculate_similarity(filename):
    left_list = []
    right_list = []
    
    # Open the file and read its contents
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers (left and right)
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Calculate and return the similarity score
    return calculate_similarity_score(left_list, right_list)

# Specify the input filename
filename = 'input.txt'

# Call the function to calculate similarity score
result = read_input_and_calculate_similarity(filename)

# Output the result
print(result)
