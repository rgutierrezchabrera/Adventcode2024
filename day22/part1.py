import sys
from typing import List

MODULO = 0xFFFFFF
ITERATIONS = 2000

def update_secret(secret: int) -> int:
    """Update the secret number based on the given rules."""
    secret = (secret ^ (secret * 64)) & MODULO
    secret = (secret ^ (secret // 32)) & MODULO
    secret = (secret ^ (secret * 2048)) & MODULO
    return secret

def get_2000th_secret_number(initial_secret: int) -> int:
    """Simulate 2000 steps to generate the 2000th secret number."""
    secret = initial_secret
    for _ in range(ITERATIONS):
        secret = update_secret(secret)
    return secret

def calculate_sum_of_2000th_secret_numbers(initial_secrets: List[int]) -> int:
    """Calculate the sum of the 2000th secret numbers for all buyers."""
    return sum(get_2000th_secret_number(secret) for secret in initial_secrets)

def read_input_file(file_path: str) -> List[int]:
    """Read the input from a file and return a list of integers."""
    with open(file_path, 'r') as f:
        return [int(line.strip()) for line in f]

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    
    try:
        initial_secrets = read_input_file(input_file)
        result = calculate_sum_of_2000th_secret_numbers(initial_secrets)
        print(f"Answer to Part One: {result}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input in the file. All lines should contain valid integers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
