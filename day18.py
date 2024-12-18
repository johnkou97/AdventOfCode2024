if __name__ == "__main__":
    import numpy as np
    from day16 import NumberOfTiles # nice that we get to reuse code from previous days

    with open("inputs/day18.txt") as f:
        data = f.read().splitlines()

    # split data with commas and convert to integers
    data = [row.split(",") for row in data]
    data = [[int(num) for num in row] for row in data]
    data = np.array(data)

    # Create a grid
    size = 71

    grid_init = np.full((size, size), ".")
    grid_init[0, 0] = "S"
    grid_init[size - 1, size - 1] = "E"

    # Part 1 - Shortest path for the first 1024 bytes

    n_bytes = 1024
    grid = grid_init.copy()
    for i, row in enumerate(data):
        x, y = row[:2]
        grid[x, y] = "#"
        if i == n_bytes - 1:
            break

    # we will use the NumberOfTiles function from Day 16
    # to make it work for this problem, we need to set the cost of turning to a very small number
    # this will prevent the robot from getting stuck in a loop (always turning and not moving forward)
    # while at the same time, it will not punish the robot for turning like in the previous problem (Day 16)
    score, _ = NumberOfTiles(grid, cost_forward=1, cost_turn=1e-6)
    print(f"Minimum number of steps to reach the end: {score}")

    # Part 2 - First byte that blocks the exit

    # Binary search to find the first byte that blocks the exit
    checked_low = n_bytes
    checked_high = len(data)

    while checked_low < checked_high:
        n_bytes = (checked_low + checked_high) // 2
        # Reset the grid
        grid = grid_init.copy()
        for i, row in enumerate(data):
            x, y = row[:2]
            grid[x, y] = "#"
            if i == n_bytes - 1:
                break

        _, num_tiles = NumberOfTiles(grid, cost_forward=1, cost_turn=1e-6)
        if num_tiles == 0:
            checked_high = n_bytes
        else:
            checked_low = n_bytes + 1

    print(f"First byte that blocks the exit: {x},{y}")
