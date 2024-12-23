import sys
from collections import Counter
from typing import Tuple, Iterator

MODULO = 0xFFFFFF
SEQUENCE_LENGTH = 4
ITERATIONS = 2000

def update_secret(secret: int) -> int:
    """Update the secret number based on the given rules."""
    secret = (secret ^ (secret * 64)) & MODULO
    secret = (secret ^ (secret // 32)) & MODULO
    secret = (secret ^ (secret * 2048)) & MODULO
    return secret

def process_secret(secret: int) -> Iterator[Tuple[Tuple[int, ...], int]]:
    """Process a secret number to generate price changes and sequences."""
    last_price = secret % 10
    changes = []
    seen = set()

    for _ in range(ITERATIONS):
        secret = update_secret(secret)
        price = secret % 10
        diff = price - last_price
        last_price = price
        changes.append(diff)

        if len(changes) >= SEQUENCE_LENGTH:
            seq = tuple(changes[-SEQUENCE_LENGTH:])
            if seq not in seen:
                seen.add(seq)
                yield seq, price

def main():
    sequences = Counter()
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    
    try:
        with open(input_file) as f:
            for line in f:
                secret = int(line.strip())
                for seq, price in process_secret(secret):
                    sequences[seq] += price
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input in the file. All lines should contain valid integers.")
        sys.exit(1)

    max_bananas = sequences.most_common(1)[0][1]
    print(f"Answer to Part Two: {max_bananas}")

if __name__ == "__main__":
    main()
