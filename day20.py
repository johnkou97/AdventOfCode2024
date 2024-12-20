import numpy as np

# Movement offsets for traversal
DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def FindMainPath(grid: np.array) -> list:
    '''
    Finds the main path from start to end.
    Uses a simple backtracking algorithm to find the path.
    Utilizes the fact that there is only one path from start to end
    '''
    start_position = tuple(np.argwhere(grid == "S")[0])
    end_position = tuple(np.argwhere(grid == "E")[0])
    
    path = [start_position]
    while path[-1] != end_position:
        x, y = path[-1]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]):
                continue
            if len(path) > 1 and (nx, ny) == path[-2]:  # Avoid backtracking
                continue
            if grid[nx][ny] == "#":  # Skip walls
                continue
            path.append((nx, ny))
            break
    return path

def CalculateCheats(grid: np.array, cheating_time: int = 2, threshold: int = 100) -> int:
    '''
    Calculates the number of points that save at least threshold picoseconds 
    by cheating for cheating_time picoseconds.
    Utilizes the main path to calculate the savings.
    Uses a brute force approach to calculate the savings.
    '''
    # Find the main path from start to end
    main_path = FindMainPath(grid)

    time_remaining = {}
    for time, position in enumerate(main_path):
        time_remaining[position] = len(main_path) - 1 - time

    savings = {}

    for time, position in enumerate(main_path):
        x, y = position
        for nx in range(x - cheating_time, x + cheating_time + 1):
            for ny in range(y - cheating_time, y + cheating_time + 1):
                if not (0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]):
                    continue
                distance_cost = abs(nx - x) + abs(ny - y)
                if distance_cost > cheating_time or grid[nx][ny] == "#":
                    continue

                remaining_time = time_remaining.get((nx, ny), float('-inf'))
                potential_savings = len(main_path) - 1 - (time + remaining_time + distance_cost)

                if potential_savings >= threshold:
                    savings[(x, y, nx, ny)] = potential_savings

    return sum(1 for value in savings.values() if value >= threshold)


if __name__ == "__main__":
    with open("inputs/day20.txt") as file:
        input_data = file.read()

    grid = input_data.splitlines()
    grid = [list(row) for row in grid]
    grid = np.array(grid)

    # Part 1 - Number of cheats that save 100 picoseconds

    threshold = 100
    cheating_time = 2
    cheats = CalculateCheats(grid, cheating_time, threshold)
    print(f"Number of points that save at least {threshold} picoseconds (Part 1): {cheats}")

    
    # Part 2 - Number of cheats that save 100 picoseconds with cheating of 20 picoseconds

    threshold = 100
    cheating_time = 20
    cheats_20 = CalculateCheats(grid, cheating_time, threshold)
    print(f"Number of points that save at least {threshold} picoseconds (Part 2): {cheats_20}")

