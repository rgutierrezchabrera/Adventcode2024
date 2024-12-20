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

def can_make_design_dp(design, towel_patterns):
    """
    Check if a design can be constructed using the available towel patterns with dynamic programming (DP).

    Args:
        design (str): The design to check.
        towel_patterns (list): List of available towel patterns.

    Returns:
        bool: True if the design can be constructed, False otherwise.
    """
    n = len(design)  # Length of the design

    # DP table: dp[i] indicates whether the first i characters of the design can be formed
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: an empty design can always be formed

    # Fill the DP table
    for i in range(1, n + 1):
        for pattern in towel_patterns:
            # Check if the pattern matches the current end of the design
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[n]

def count_possible_designs(towel_patterns, desired_designs):
    """
    Count how many designs can be constructed using the available towel patterns.

    Args:
        towel_patterns (list): List of available towel patterns.
        desired_designs (list): List of desired designs to be checked.

    Returns:
        int: The number of designs that can be constructed.
    """
    return sum(1 for design in desired_designs if can_make_design_dp(design, towel_patterns))

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
example_result = count_possible_designs(towel_patterns, desired_designs)
assert example_result == 6, f"Example test failed, got {example_result}"  # Expected result is 6

print(f"Example Test Passed! Result: {example_result}")

# Process Input from File
with open("input.txt") as f:
    file_input = f.read()

# Parse File Input
towel_patterns, desired_designs = parse_input(file_input)

# Calculate Result for File Input
file_result = count_possible_designs(towel_patterns, desired_designs)
print(f"Result for input.txt: {file_result}")