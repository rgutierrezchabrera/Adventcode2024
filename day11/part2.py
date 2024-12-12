import time

def calculate_iterations(number, iterations, result_table):
    if iterations == 0:
        return 1
    
    # Check if the result is already computed
    if (number, iterations) in result_table:
        return result_table[(number, iterations)]

    if number == 0:
        result = calculate_iterations(1, iterations - 1, result_table)
    else:
        digits = len(str(number))
        if digits % 2 == 0:
            mid = digits // 2
            left = int(str(number)[:mid])
            right = int(str(number)[mid:])
            result = (calculate_iterations(left, iterations - 1, result_table) +
                      calculate_iterations(right, iterations - 1, result_table))
        else:
            result = calculate_iterations(number * 2024, iterations - 1, result_table)

    # Store the computed result in the table
    result_table[(number, iterations)] = result
    return result

def precompute_iterations(max_number, iterations):
    result_table = {}
    
    for num in range(max_number + 1):
        calculate_iterations(num, iterations, result_table)

    return result_table

def total_stone_count(input_list, iterations, result_table):
    total_count = 0
    for number in input_list:
        if number > max(result_table.keys())[0]:
            # Handle numbers larger than max_number
            total_count += calculate_iterations(number, iterations, result_table)
        else:
            total_count += result_table.get((number, iterations), 1)
    return total_count

# Your input
input_stones = [7568, 155731, 0, 972, 1, 6919238, 80646, 22]
max_number = max(input_stones)  # Or set to a higher value if memory allows
iterations = 75

# Start the timer
start_time = time.time()

# Precompute results
result_table = precompute_iterations(max_number, iterations)

# Calculate final result
result = total_stone_count(input_stones, iterations, result_table)

# Stop the timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

print(f"Final number of stones after {iterations} blinks: {result}")
print(f"Execution time: {execution_time:.2f} seconds")
