if __name__ == '__main__':
    import numpy as np

    with open("inputs/day8.txt") as f:
        data = f.read().splitlines()
    
    data = np.array([np.array(list(row)) for row in data])

    # Part 1 - Number of unique antinodes

    # create a list of unique characters (disregard .)
    unique_chars = np.unique(data)
    unique_chars = unique_chars[unique_chars != '.']

    # find position of antinodes
    map_antinode = np.zeros(data.shape, dtype=int)
    for char in unique_chars:
        # get locations of char
        locs_x, locs_y = np.where(data == char)
        for i, (x_1, y_1) in enumerate(zip(locs_x, locs_y)):
            # get locations of all other chars
            for x_2, y_2 in zip(locs_x[i+1:], locs_y[i+1:]):
                if 2*x_1 - x_2 < 0 or 2*x_1 - x_2 >= data.shape[0] or 2*y_1 - y_2 < 0 or 2*y_1 - y_2 >= data.shape[1]:
                    pass
                else:
                    map_antinode[2*x_1 - x_2, 2*y_1 - y_2] = 1
                if 2*x_2 - x_1 < 0 or 2*x_2 - x_1 >= data.shape[0] or 2*y_2 - y_1 < 0 or 2*y_2 - y_1 >= data.shape[1]:
                    pass
                else:
                    map_antinode[2*x_2 - x_1, 2*y_2 - y_1] = 1
                    
    print(f"Number of antinodes: {np.sum(map_antinode)}")

    # Part 2 - Number of unique antinodes with resonant harmonics

    # find position of antinodes
    map_antinode_resonant = np.zeros(data.shape, dtype=int)
    for char in unique_chars:
        # get locations of char
        locs_x, locs_y = np.where(data == char)
        for i, (x_1, y_1) in enumerate(zip(locs_x, locs_y)):
            # get locations of all other chars
            for x_2, y_2 in zip(locs_x[i+1:], locs_y[i+1:]):
                # get all resonant harmonics
                a = 0
                while True:
                    if (a+1)*x_1 - a*x_2 < 0 or (a+1)*x_1 - a*x_2 >= data.shape[0] or (a+1)*y_1 - a*y_2 < 0 or (a+1)*y_1 - a*y_2 >= data.shape[1]:
                        break
                    else:
                        map_antinode_resonant[(a+1)*x_1 - a*x_2, (a+1)*y_1 - a*y_2] = 1
                    a += 1
                a = 0
                while True:
                    if (a+1)*x_2 - a*x_1 < 0 or (a+1)*x_2 - a*x_1 >= data.shape[0] or (a+1)*y_2 - a*y_1 < 0 or (a+1)*y_2 - a*y_1 >= data.shape[1]:
                        break
                    else:
                        map_antinode_resonant[(a+1)*x_2 - a*x_1, (a+1)*y_2 - a*y_1] = 1
                    a += 1

    print(f"Number of antinodes with resonant harmonics: {np.sum(map_antinode_resonant)}")