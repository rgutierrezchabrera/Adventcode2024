def is_safe(report):
    levels = list(map(int, report.split()))
    is_increasing = all(0 < levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_decreasing = all(-3 <= levels[i + 1] - levels[i] < 0 for i in range(len(levels) - 1))
    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    levels = list(map(int, report.split()))
    
    # If the report is already safe
    if is_safe(report):
        return True
    
    # Try removing each level
    for i in range(len(levels)):
        # Create a new sequence without the i-th level
        modified_report = levels[:i] + levels[i + 1:]
        # Check if the modified sequence is safe
        if is_safe(" ".join(map(str, modified_report))):
            return True
    
    # If no modification makes it safe
    return False

def count_safe_reports_with_dampener(file_name):
    safe_count = 0
    
    with open(file_name, 'r') as file:
        for line in file:
            if is_safe_with_dampener(line.strip()):
                safe_count += 1
                
    return safe_count

# Run the function with the input file
input_file = 'input.txt'
print("Number of safe reports (with dampener):", count_safe_reports_with_dampener(input_file))
