if __name__ == "__main__":
    import numpy as np

    with open("inputs/day6.txt") as f:
        data = f.read().splitlines()
        
    # convert to numpy array each element of each row of data
    data = np.array([np.array(list(row)) for row in data])

    # convert string to integer for faster comparison
    data = np.where(data == ".", 0, data) # denotes empty space
    data = np.where(data == "#", 1, data) # denotes wall
    data = np.where(data == "^", 2, data) # denotes guard

    # convert to integer
    data = data.astype(int)

    # Part 1 - find the number of distinct positions will the guard visit before leaving the mapped area

    # make a new copy of the data for part 1
    map_ = data.copy()

    # find the guard position
    guard = np.where(map_ == 2)
    guard = (guard[0][0], guard[1][0])

    movement = 0
    while True:
        # mark the guard position as visited 
        map_[guard] = 3 # denotes visited position
        # find the next position to move to
        if movement == 0:
            # move up
            # check if the next position is out of bounds for termination
            if guard[0] - 1 < 0:
                break
            elif map_[guard[0] - 1, guard[1]] == 1: # check if the next position is a wall for change of direction
                movement = 1
            else:
                guard = (guard[0] - 1, guard[1])
        elif movement == 1:
            # move right
            if guard[1] + 1 >= map_.shape[1]:
                break
            elif map_[guard[0], guard[1] + 1] == 1:
                movement = 2
            else:
                guard = (guard[0], guard[1] + 1)
        elif movement == 2:
            # move down
            if guard[0] + 1 >= map_.shape[0]:
                break
            elif map_[guard[0] + 1, guard[1]] == 1:
                movement = 3
            else:
                guard = (guard[0] + 1, guard[1])
        elif movement == 3:
            # move left
            if guard[1] - 1 < 0:
                break
            elif map_[guard[0], guard[1] - 1] == 1:
                movement = 0
            else:
                guard = (guard[0], guard[1] - 1)

    # count the number of visited positions
    visited = np.count_nonzero(map_ == 3)
    # keep all visited positions, useful for part 2
    visited_positions = np.where(map_ == 3)
    list_visited_positions = [(visited_positions[0][i], visited_positions[1][i]) for i in range(len(visited_positions[0]))]

    print(f"Visited positions: {visited}")

    # Part 2 - find number of positions to put a wall to make the guard stuck in a loop

    # brute force approach - try to put a wall in each visited position and check if the guard can exit the mapped area
    # if the guard can exit the mapped area, then you cannot put a wall in that position
    # let the guard move for maximum number of steps equal to the number of positions in the map (naive approach)

    number_of_walls = 0
    for position in list_visited_positions:
        # reset the data
        map_ = data.copy()

        # find the guard position (denoted by ^)
        guard = np.where(map_ == 2)
        guard = (guard[0][0], guard[1][0])

        # put a wall in the current position
        map_[position] = 1

        movement = 0
        flag_exit = False
        for _ in range(map_.size):
            # mark the guard position as visited (denoted by X)
            map_[guard] = 3
            # find the next position to move to
            if movement == 0:
                # move up
                # check if the next position is out of bounds for termination
                if guard[0] - 1 < 0:
                    flag_exit = True
                    break
                elif map_[guard[0] - 1, guard[1]] == 1:
                    movement = 1
                else:
                    guard = (guard[0] - 1, guard[1])
            elif movement == 1:
                # move right
                if guard[1] + 1 >= map_.shape[1]:
                    flag_exit = True
                    break
                elif map_[guard[0], guard[1] + 1] == 1:
                    movement = 2
                else:
                    guard = (guard[0], guard[1] + 1)
            elif movement == 2:
                # move down
                if guard[0] + 1 >= map_.shape[0]:
                    flag_exit = True
                    break
                elif map_[guard[0] + 1, guard[1]] == 1:
                    movement = 3
                else:
                    guard = (guard[0] + 1, guard[1])
            elif movement == 3:
                # move left
                if guard[1] - 1 < 0:
                    flag_exit = True
                    break
                elif map_[guard[0], guard[1] - 1] == 1:
                    movement = 0
                else:
                    guard = (guard[0], guard[1] - 1)

        # check if the guard has exited the mapped area
        if not flag_exit:
            number_of_walls += 1

    print(f"Number of walls possible: {number_of_walls}")