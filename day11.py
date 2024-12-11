from functools import lru_cache

def blink(stones):
    '''Calculate how the stones change after a blink.'''
    new_stones = []  # Use a new list to store results for this blink
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:  # check if stone has even number of digits
            half_len = len(str(stone)) // 2
            stone_1 = int(str(stone)[:half_len])
            stone_2 = int(str(stone)[half_len:])
            new_stones.append(stone_1)
            new_stones.append(stone_2)
        else:
            new_stones.append(stone * 2024)
    return new_stones

@lru_cache(None)  # Cache results to avoid redundant calculations
def count_stones(stone, blinks):
    '''
    Recursive function to calculate the number of stones after a given number of blinks.
    To be used for Part 2. Part 1 uses the blink function without recursion.
    The recursive function can of course be used for Part 1 as well, but I had already solved it with a different approach.
    '''
    if blinks == 0:
        return 1  # No further transformations; count the stone itself

    if stone == 0:
        return count_stones(1, blinks - 1)  # Transform 0 into 1

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:  # Even number of digits
        half_len = len(stone_str) // 2
        stone_1 = int(stone_str[:half_len])
        stone_2 = int(stone_str[half_len:])
        # Recursive calls for each split stone
        return count_stones(stone_1, blinks - 1) + count_stones(stone_2, blinks - 1)
    else:  # Odd number of digits
        transformed_stone = stone * 2024
        return count_stones(transformed_stone, blinks - 1)

if __name__ == "__main__":
    with open("inputs/day11.txt") as f:
        data = f.read().split(" ")

    # convert to list of integers
    data = [int(x) for x in data]

    # Part 1 - Number of stones after 25 blinks

    # blink 25 times
    for _ in range(25):
        data = blink(data)

    print(f"Number of stones after 25 blinks: {len(data)}")

    # Part 2 - Number of stones after 75 blinks

    # blink 50 more times with recursion
    total_stones = sum(count_stones(stone, 50) for stone in data)
    print(f"Number of stones after 75 blinks: {total_stones}")

    # Optional: Compare the two methods for 30 blinks (for performance testing)

    # import time
    
    # with open("inputs/day11.txt") as f:
    #     data = f.read().split(" ")
    # data = [int(x) for x in data]
    
    # # Withouth recursion
    # stones = data.copy()
    # start = time.time()
    # for _ in range(30):
    #     stones = blink(stones)
    # print(f"Without recursion: {len(stones)}")
    # time_without_recursion = time.time() - start
    # print(f"Time taken: {time_without_recursion}")
    
    # # With recursion
    # stones = data.copy()
    # start = time.time()
    # for _ in range(30):
    #     stones = [count_stones(stone, 30) for stone in stones]
    # print(f"With recursion: {sum(stones)}")
    # time_with_recursion = time.time() - start
    # print(f"Time taken: {time_with_recursion}")

    # print(f"Recursion is {time_without_recursion / time_with_recursion:.2f} times faster than without recursion!!")
