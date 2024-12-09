def is_safe(report):
    # Convert the report (a string of space-separated numbers) to a list of integers
    levels = list(map(int, report.split()))
    
    # Check if the levels are consistently increasing or decreasing with valid step differences
    is_increasing = all(0 < levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_decreasing = all(-3 <= levels[i + 1] - levels[i] < 0 for i in range(len(levels) - 1))
    
    return is_increasing or is_decreasing

def count_safe_reports(file_name):
    safe_count = 0
    
    with open(file_name, 'r') as file:
        for line in file:
            if is_safe(line.strip()):
                safe_count += 1
                
    return safe_count

# Run the function with the input file
input_file = 'input.txt'
print("Number of safe reports:", count_safe_reports(input_file))
