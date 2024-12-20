def parse_input(input_data):
    """
    Parse the input data into towel patterns and desired designs.

    Args:
        input_data (str): The raw input string containing towel patterns and desired designs.

    Returns:
        tuple: A list of towel patterns and a list of desired designs.
    """
    # Split the input into two sections: towel patterns and desired designs
    sections = input_data.strip().split("\n\n")

    # First section contains towel patterns, separated by commas
    towel_patterns = sections[0].split(", ")

    # Second section contains desired designs, each on a new line
    desired_designs = sections[1].splitlines()

    return towel_patterns, desired_designs

def count_arrangements(design, towel_patterns):
    """
    Count all possible arrangements of towel patterns to form a given design.

    Args:
        design (str): The design to be formed.
        towel_patterns (list): List of available towel patterns.

    Returns:
        int: Total number of ways to arrange towel patterns to form the design.
    """
    # Memoization dictionary to store intermediate results
    memo = {}

    def backtrack(remaining_design):
        """
        Recursive helper function to count arrangements for the remaining part of the design.

        Args:
            remaining_design (str): The portion of the design yet to be formed.

        Returns:
            int: Number of ways to arrange patterns to form the remaining design.
        """
        if remaining_design in memo:
            return memo[remaining_design]  # Return cached result
        if not remaining_design:
            return 1  # One valid way to form an empty design

        ways = 0
        for pattern in towel_patterns:
            # Check if the pattern matches the start of the remaining design
            if remaining_design.startswith(pattern):
                ways += backtrack(remaining_design[len(pattern):])

        memo[remaining_design] = ways  # Cache the result
        return ways

    return backtrack(design)

def total_arrangements(towel_patterns, desired_designs):
    """
    Calculate the total number of arrangements for all designs.

    Args:
        towel_patterns (list): List of available towel patterns.
        desired_designs (list): List of desired designs to be checked.

    Returns:
        int: Sum of all possible arrangements for all designs.
    """
    return sum(count_arrangements(design, towel_patterns) for design in desired_designs)

# Example Input
test_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

# Parse Example Input
towel_patterns, desired_designs = parse_input(test_input)

# Validate Example Input
example_result = total_arrangements(towel_patterns, desired_designs)
assert example_result == 16, f"Example test failed, got {example_result}"  # Expected result is 16

print(f"Example Test Passed! Result: {example_result}")

# Process Input from File
with open("input.txt") as f:
    file_input = f.read()

# Parse File Input
towel_patterns, desired_designs = parse_input(file_input)

# Calculate Result for File Input
file_result = total_arrangements(towel_patterns, desired_designs)
print(f"Result for input.txt: {file_result}")