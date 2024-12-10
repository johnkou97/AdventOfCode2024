def count_paths(trail_map, data, x, y, step):
    '''
    Recursive function to count distinct paths.
    Used to solve Part 2. 
    A recursive approach might also be useful for Part 1, but I had already solved it with a different approach.
    '''
    if data[x, y] == 9:
        return 1  # Found a valid path ending at 9

    path_count = 0
    next_step = step + 1

    # Explore all valid directions
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < data.shape[0]
            and 0 <= ny < data.shape[1]
            and data[nx, ny] == next_step
            and trail_map[nx, ny] == -1  # Unvisited
        ):
            # Mark this position as visited
            trail_map[nx, ny] = next_step
            path_count += count_paths(trail_map, data, nx, ny, next_step)
            # Backtrack to allow other paths
            trail_map[nx, ny] = -1

    return path_count

if __name__ == "__main__":
    import numpy as np

    with open("inputs/day10.txt") as f:
        data = f.read().splitlines()

    data = np.array([[int(i) for i in list(row)] for row in data])

    # find all starting points
    start_points = np.argwhere(data == 0)

    # Part 1 - Sum of scores of trailheads

    # find scores of all trailheads
    score = 0
    for start_point in start_points:
        x, y = start_point
        trail_map = np.full(data.shape, -1)
        trail_map[x, y] = 0
        for step in range(9):
            # find all points in map that have value step
            points = np.argwhere(trail_map == step)
            for point in points:
                x, y = point
                # check all 4 directions for valid points and update trail_map
                if x - 1 >= 0 and data[x - 1, y] == step + 1:
                    trail_map[x - 1, y] = step + 1
                if x + 1 < data.shape[0] and data[x + 1, y] == step + 1:
                    trail_map[x + 1, y] = step + 1
                if y - 1 >= 0 and data[x, y - 1] == step + 1:
                    trail_map[x, y - 1] = step + 1
                if y + 1 < data.shape[1] and data[x, y + 1] == step + 1:
                    trail_map[x, y + 1] = step + 1
        score += np.sum(trail_map == 9)

    print(f"Sum of scores of trailheads: {score}")

    # Part 2 - Number of ratings of trailheads

    rating = 0
    for start_point in start_points:
        x, y = start_point
        trail_map = np.full(data.shape, -1)
        trail_map[x, y] = 0  # Mark start point as visited
        rating += count_paths(trail_map, data, x, y, 0)

    print(f"Number of ratings of trailheads: {rating}")
