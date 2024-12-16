import heapq
import numpy as np

def NumberOfTiles(grid: np.array) -> tuple:
    '''
    Calculate the score and number of unique tiles in the winning paths
    '''
    # Locate the start (S) and end (E) positions
    start = tuple(np.argwhere(grid == 'S')[0])
    end = tuple(np.argwhere(grid == 'E')[0])

    # Convert the 'E' to a walkable tile for easier processing
    grid[end[0]][end[1]] = '.'

    # Priority queue: (score, direction, x, y, path_so_far)
    pq = []
    heapq.heappush(pq, (0, 0, start[0], start[1], {start}))
    visited = {}
    score = 1e69
    tiles = []

    while pq:
        new_score, dir, x, y, path = heapq.heappop(pq)

        # If a lower score has already been found, we can stop processing
        if score < new_score:
            break

        # If we've reached the end
        if (x, y) == end:
            if score == 1e69:
                score = new_score  # Record the lowest score
            if new_score == score:
                tiles.extend(path)
            continue

        if (dir, x, y) in visited and visited[(dir, x, y)] < new_score:
            continue
        visited[(dir, x, y)] = new_score

        # Move in
        if dir == 0:
            nx, ny = x, y + 1
        elif dir == 1:
            nx, ny = x + 1, y
        elif dir == 2:
            nx, ny = x, y - 1
        else:
            nx, ny = x - 1, y

        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx][ny] != '#':
            heapq.heappush(pq, (new_score + 1, dir, nx, ny, path | {(nx, ny)}))

        # Turn left or right
        for turn in [-1, 1]:
            new_dir = (dir + turn) % 4
            heapq.heappush(pq, (new_score + 1000, new_dir, x, y, path))

    # The lowest score and the number of unique tiles in all winning paths
    return score, len(set(tiles))


if __name__ == "__main__":

    with open("inputs/day16.txt") as f:
        data = f.read()

    # split data into single characters and turn to numpy array
    data = data.splitlines()
    data = [list(row) for row in data]
    data = np.array(data)

    # Part 1 - Score of the shortest path
    
    # Part 2 - Number of unique tiles in all winning paths

    score, num_tiles = NumberOfTiles(data)

    print(f"Score of the shortest path: {score}")
    print(f"Number of unique tiles in all winning paths: {num_tiles}")