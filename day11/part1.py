def transform_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        return [int(str(stone)[:mid]), int(str(stone)[mid:])]
    else:
        return [stone * 2024]

def blink(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(transform_stone(stone))
    return new_stones

def count_stones_after_blinks(initial_stones, blinks):
    stones = initial_stones
    for _ in range(blinks):
        stones = blink(stones)
    return len(stones)

# Example input
example_stones = [125, 17]

# Calculate result for example
example_result = count_stones_after_blinks(example_stones, 25)

# Check if example result matches expected output
expected_result = 55312
if example_result == expected_result:
    print("Test works! The algorithm produces the correct result for the example.")
    
    # Process input from file
    try:
        with open('input.txt', 'r') as file:
            input_stones = list(map(int, file.read().split()))
        
        final_result = count_stones_after_blinks(input_stones, 25)
        print(f"Number of stones after 25 blinks (input file): {final_result}")
    except FileNotFoundError:
        print("Error: input.txt file not found.")
    except Exception as e:
        print(f"An error occurred while processing the input file: {e}")
else:
    print(f"Test failed. Expected {expected_result}, but got {example_result}")

# Print the example result
print(f"Number of stones after 25 blinks (example): {example_result}")
