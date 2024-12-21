from part1 import get_data, count_cheats

def part_2(grid, max_cheat_time=20, minimal_cheat=100):
    """
    Solves Part 2 of the puzzle by extending the max_cheat_time and minimal_cheat constraints.

    Args:
        grid (list): The grid as a list of strings.
        max_cheat_time (int): Maximum time a cheat can save.
        minimal_cheat (int): Minimum cheat saving to be considered.
    
    Returns:
        int: The number of cheats with time savings >= minimal_cheat for the new constraints.
    """
    cheats = count_cheats(grid, max_cheat_time)
    return sum(count for time, count in cheats.items() if time >= minimal_cheat)

def main():
    """
    Main function to run Part 2 of the puzzle.
    """
    with open('input.txt') as input_file:  # Open the input file
        grid = get_data(input_file)
    
    result = part_2(grid)
    print(f"Part 2 Result: {result}")

if __name__ == "__main__":
    main()
