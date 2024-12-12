from collections import deque
import numpy as np

def count_unique_sides(region):
    '''
    Calculate the number of unique edges in a region.
    To do this, we iterate through all the cells in the region.
    For each cell, we check if it has a neighbor that is not part of the same region.
    For example, for the top edge, we check if the top neighbor is not part of the region.
    If it's not part of the region, then it's an edge. But we also need to check if it's a new edge.
    It is not a new edge if the cell to the left of the current cell is part of the region, 
    and the top-left cell is not part of the region (or out of bounds).
    '''
    edges = 0
    for r in range(region.shape[0]):
        for c in range(region.shape[1]):
            if region[r, c] == 0:
                continue

            north_n = (r - 1, c)
            west_n = (r, c - 1)
            nw_n = (r - 1, c - 1)
            if north_n[0] >= 0:
                if region[north_n] == 0:
                    if west_n[1] >= 0:
                        same_edge = (region[west_n] != 0) and (region[nw_n] == 0)
                        if not same_edge:
                            edges += 1
                    else:
                        edges += 1
            else:
                if west_n[1] < 0:
                    edges += 1
                else:
                    same_edge = (region[west_n] != 0)
                    if not same_edge:
                        edges += 1

            south_n = (r + 1, c)
            sw_n = (r + 1, c - 1)
            if south_n[0] < region.shape[0]:
                if region[south_n] == 0:
                    if west_n[1] >= 0:
                        same_edge = (region[west_n] != 0) and (region[sw_n] == 0)
                        if not same_edge:
                            edges += 1
                    else:
                        edges += 1
            else:
                if west_n[1] < 0:
                    edges += 1
                else:
                    same_edge = (region[west_n] != 0)
                    if not same_edge:
                        edges += 1

            if west_n[1] >= 0:
                if region[west_n] == 0:
                    if north_n[0] >= 0:
                        same_edge = (region[north_n] != 0) and (region[nw_n] == 0)
                        if not same_edge:
                            edges += 1
                    else:
                        edges += 1
            else:
                if north_n[0] < 0:
                    edges += 1
                else:
                    same_edge = (region[north_n] != 0)
                    if not same_edge:
                        edges += 1

            east_n = (r, c + 1)
            ne_n = (r - 1, c + 1)
            if east_n[1] < region.shape[1]:
                if region[east_n] == 0:
                    if north_n[0] >= 0:
                        same_edge = (region[north_n] != 0) and (region[ne_n] == 0)
                        if not same_edge:
                            edges += 1
                    else:
                        edges += 1
            else:
                if north_n[0] < 0:
                    edges += 1
                else:
                    same_edge = (region[north_n] != 0)
                    if not same_edge:
                        edges += 1

    return edges

def bfs(x, y):
    '''
    Perform BFS to find the region area and perimeter.
    Created by ChatGPT, and only used for the ChatGPT solution.
    My solution does not use this function.
    '''
    queue = deque([(x, y)])
    visited[x, y] = True
    region_type = data[x, y]
    area = 0
    perimeter = 0

    while queue:
        cx, cy = queue.popleft()
        area += 1
        # Check all 4 neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:  # Valid cell
                if data[nx, ny] == region_type and not visited[nx, ny]:
                    visited[nx, ny] = True
                    queue.append((nx, ny))
                elif data[nx, ny] != region_type:  # Neighboring cell is different
                    perimeter += 1
            else:
                # Out of bounds, contributes to perimeter
                perimeter += 1

    return area, perimeter

if __name__ == '__main__':
    import numpy as np

    with open("inputs/day12.txt") as f:
        data = f.read().splitlines()
    
    data = np.array([np.array(list(row)) for row in data])

    cost_perimeter = 0      # used for part 1
    cost_sides = 0          # used for part 2
    regions_map = np.zeros_like(data, dtype=int)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if regions_map[i, j] == 0:
                regions_map[i, j] = 1
                current_region = np.zeros_like(data, dtype=int)
                current_region[i, j] = 1
                count = 2
                while True:
                    # find all the cells in the current region with value equal to count-1
                    indices = np.argwhere(current_region == count-1)
                    for index in indices:
                        x, y = index
                        if x > 0 and data[x-1, y] == data[x, y] and current_region[x-1, y] == 0:
                            regions_map[x-1, y] = 1
                            current_region[x-1, y] = count
                        if x < data.shape[0]-1 and data[x+1, y] == data[x, y] and current_region[x+1, y] == 0:
                            regions_map[x+1, y] = 1
                            current_region[x+1, y] = count
                        if y > 0 and data[x, y-1] == data[x, y] and current_region[x, y-1] == 0:
                            regions_map[x, y-1] = 1
                            current_region[x, y-1] = count
                        if y < data.shape[1]-1 and data[x, y+1] == data[x, y] and current_region[x, y+1] == 0:
                            regions_map[x, y+1] = 1
                            current_region[x, y+1] = count    
                        
                    if not np.any(current_region == count):
                        break
                    count += 1

                # Part 1 - Find cost of fencing all the regions

                # calculate the cost of fencing the region as area * perimeter
                # area is the number of cells in the region
                area = np.sum(current_region != 0)
                # perimeter is more complicated. You need to find all the non-same value neighbours of every cell in the region
                perimeter = 0
                for x in range(data.shape[0]):
                    for y in range(data.shape[1]):
                        if current_region[x, y] != 0:
                            if x == 0 or current_region[x-1, y] == 0:
                                perimeter += 1
                            if x == data.shape[0]-1 or current_region[x+1, y] == 0:
                                perimeter += 1
                            if y == 0 or current_region[x, y-1] == 0:
                                perimeter += 1
                            if y == data.shape[1]-1 or current_region[x, y+1] == 0:
                                perimeter += 1
                cost_perimeter += area * perimeter

                # Part 2 - Find cost of fencing all the regions but only counting sides and not total perimeter

                # calculate the cost of fencing the region as area * sides
                # area is the number of cells in the region
                area = np.sum(current_region != 0)
                # sides is more complicated. 
                # use function count_unique_sides to find the number of unique sides in the region
                sides = count_unique_sides(current_region)
                cost_sides += area * sides
                
    print(f"Total cost with perimeter: {cost_perimeter}")
    print(f"Total cost with only sides: {cost_sides}")

    # Optional: ChatGPT solution using BFS for: Part 1 - Find cost of fencing all the regions

    print("ChatGPT solution using BFS")

    rows, cols = data.shape
    visited = np.zeros_like(data, dtype=bool)  # Track visited cells
    cost = 0

    # Iterate over all cells in the grid
    for i in range(rows):
        for j in range(cols):
            if not visited[i, j]:  # Found a new region
                area, perimeter = bfs(i, j)
                cost += area * perimeter

    print(f"Total cost: {cost}")