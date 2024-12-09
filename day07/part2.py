from itertools import product

def parse_input(file_path):
    """Parse the input file and return a list of test values and equations."""
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            target, numbers = line.strip().split(':')
            target = int(target)
            numbers = list(map(int, numbers.split()))
            equations.append((target, numbers))
    return equations

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression formed by inserting the operators between numbers.
    Operators are applied left-to-right, not by mathematical precedence.
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            # Concatenate digits of the numbers
            result = int(str(result) + str(numbers[i + 1]))
    return result

def find_valid_equations(equations):
    """
    Determine which equations can be made valid and compute the total calibration result.
    """
    total_calibration_result = 0
    
    for target, numbers in equations:
        num_operators = len(numbers) - 1
        valid = False
        
        # Generate all combinations of operators ('+', '*', '||') for the equation
        for operators in product(['+', '*', '||'], repeat=num_operators):
            result = evaluate_expression(numbers, operators)
            if result == target:
                valid = True
                break
        
        if valid:
            total_calibration_result += target
    
    return total_calibration_result

if __name__ == "__main__":
    # Step 1: Parse the input
    input_file = "input.txt"
    equations = parse_input(input_file)
    
    # Step 2: Find valid equations and compute the result
    total_result = find_valid_equations(equations)
    
    # Step 3: Output the result
    print(f"Total Calibration Result: {total_result}")
