import numpy as np

def render(maze, name=None):
    '''
    Function to render the maze
    Useful for debugging
    '''
    import matplotlib.pyplot as plt # we need to import this here, as it is not used in the main code
    from matplotlib.colors import ListedColormap

    cmap = ListedColormap(['white', 'black', 'blue', 'red', 'green'])

    plt.figure(figsize=(10,10))
    plt.imshow(maze, cmap=cmap)
    if name is not None:
        plt.savefig(f'outputs/{name}.png')
        plt.close()
    else:
        plt.show()

def move(maze, ins):
    '''
    Function to move the agent in the maze
    The agent can move in 4 directions: right(0), down(1), left(2), up(3)
    The agent can move to an empty space or push a box
    If the agent pushes a box, the box will move to the next empty space
    If there is a wall in front of the agent or the box, the agent will not move
    The agent can move multiple boxes at once, as long as there is an empty space in front of the last box
    The agent is represented by 3, the box is represented by 2, the wall is represented by 1, and the empty space is represented by 0
    There is no need to check if the agent gets out of the maze, as it is protected by walls
    The function will return the maze after the agent moves
    '''
    # find the agent
    x, y = np.where(maze == 3)
    agent = (x[0], y[0])

    if ins == 0: # right
        if maze[agent[0]][agent[1]+1] == 0: # found empty space
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]][agent[1]+1] = 3
        elif maze[agent[0]][agent[1]+1] == 2: # found box
            # count how many boxes are in front of the box
            count = 0
            for j in range(agent[1]+1, len(maze[0])):
                if maze[agent[0]][j] == 2:
                    count += 1
                else:
                    break
            # check if there is an empty space in front of the box
            if maze[agent[0]][agent[1]+1+count] == 0:
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]][agent[1]+1] = 3
                maze[agent[0]][agent[1]+1+count] = 2
    elif ins == 1: # down
        if maze[agent[0]+1][agent[1]] == 0:
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]+1][agent[1]] = 3
        elif maze[agent[0]+1][agent[1]] == 2:
            count = 0
            for j in range(agent[0]+1, len(maze)):
                if maze[j][agent[1]] == 2:
                    count += 1
                else:
                    break
            if maze[agent[0]+1+count][agent[1]] == 0:
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]+1][agent[1]] = 3
                maze[agent[0]+1+count][agent[1]] = 2
    elif ins == 2: # left
        if maze[agent[0]][agent[1]-1] == 0:
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]][agent[1]-1] = 3
        elif maze[agent[0]][agent[1]-1] == 2:
            count = 0
            for j in range(agent[1]-1, -1, -1):
                if maze[agent[0]][j] == 2:
                    count += 1
                else:
                    break
            if maze[agent[0]][agent[1]-1-count] == 0:
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]][agent[1]-1] = 3
                maze[agent[0]][agent[1]-1-count] = 2
    elif ins == 3: # up
        if maze[agent[0]-1][agent[1]] == 0:
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]-1][agent[1]] = 3
        elif maze[agent[0]-1][agent[1]] == 2:
            count = 0
            for j in range(agent[0]-1, -1, -1):
                if maze[j][agent[1]] == 2:
                    count += 1
                else:
                    break
            if maze[agent[0]-1-count][agent[1]] == 0:
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]-1][agent[1]] = 3
                maze[agent[0]-1-count][agent[1]] = 2

    return maze

def move_2(maze, ins):
    '''
    Same as move function, but with boxes that have double size
    Left side of the box is represented by 2, right side of the box is represented by 4
    Does not work perfectly, but it is a good start
    '''
    # find the agent
    x, y = np.where(maze == 3)
    agent = (x[0], y[0])

    if ins == 0: # right
        if maze[agent[0]][agent[1]+1] == 0: # found empty space
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]][agent[1]+1] = 3
        elif maze[agent[0]][agent[1]+1] == 2 or maze[agent[0]][agent[1]+1] == 4: # found box
            # count how many boxes are in front of the box
            count = 0
            for j in range(agent[1]+1, len(maze[0])):
                if maze[agent[0]][j] == 2 or maze[agent[0]][j] == 4:
                    count += 1 # this counts each box double, but it fine for now
                else:
                    break
            # check if there is an empty space in front of the box
            if maze[agent[0]][agent[1]+1+count] == 0:
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]][agent[1]+1] = 3
                for j in range(int(count/2)):
                    maze[agent[0]][agent[1]+2+2*j] = 2
                    maze[agent[0]][agent[1]+2+2*j+1] = 4  # might be a bug here
    elif ins == 1: # down
        if maze[agent[0]+1][agent[1]] == 0:
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]+1][agent[1]] = 3
        elif maze[agent[0]+1][agent[1]] == 2 or maze[agent[0]+1][agent[1]] == 4:
            count = 0 # this time we have to pottenially count boxes in multiple columns
            y_to_look = np.array([agent[1]])
            y_to_move = [np.array([agent[1]])]
            move = True
            for j in range(agent[0]+1, len(maze)):
                all_zeros = True
                y_new = y_to_move[-1]
                for k in y_to_look:
                    if maze[j][k] == 2: # left side of the box, add the right side to y_to_look
                        if maze[j-1][k] == 0: # might be a bug here
                            continue
                        all_zeros = False
                        if k+1 not in y_new: # y_new is an array
                            y_new = np.append(y_new, k+1)
                            y_new = np.sort(y_new)
                        if k+1 not in y_to_look:
                            y_to_look = np.append(y_to_look, k+1)
                            y_to_look = np.sort(y_to_look)
                    elif maze[j][k] == 4: # right side of the box, add the left side to y_to_look
                        if maze[j-1][k] == 0: # might be a bug here
                            continue
                        all_zeros = False
                        if k-1 not in y_new:
                            y_new = np.append(y_new, k-1)
                            y_new = np.sort(y_new)
                        if k-1 not in y_to_look:
                            y_to_look = np.append(y_to_look, k-1)
                            y_to_look = np.sort(y_to_look)
                    elif maze[j][k] == 1: # wall, break the loop and do not move anything
                        move = False
                        break
                y_to_move.append(y_new)
                if all_zeros:
                    break
                else:
                    count += 1
            if move:
                for j in range(count, 0, -1):
                    for k in y_to_move[j]:
                        if maze[agent[0]+j][k] == 2:
                            maze[agent[0]+j+1][k] = 2
                            maze[agent[0]+j][k] = 0
                        elif maze[agent[0]+j][k] == 4:
                            maze[agent[0]+j+1][k] = 4
                            maze[agent[0]+j][k] = 0
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]+1][agent[1]] = 3
    elif ins == 2: # left (similar to right)
        if maze[agent[0]][agent[1]-1] == 0:
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]][agent[1]-1] = 3
        elif maze[agent[0]][agent[1]-1] == 2 or maze[agent[0]][agent[1]-1] == 4:
            count = 0
            for j in range(agent[1]-1, -1, -1):
                if maze[agent[0]][j] == 2 or maze[agent[0]][j] == 4:
                    count += 1
                else:
                    break
            if maze[agent[0]][agent[1]-1-count] == 0:
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]][agent[1]-1] = 3
                for j in range(int(count/2)):
                    maze[agent[0]][agent[1]-2-2*j] = 4
                    maze[agent[0]][agent[1]-2-2*j-1] = 2
    elif ins == 3: # up (similar to down)
        if maze[agent[0]-1][agent[1]] == 0:
            maze[agent[0]][agent[1]] = 0
            maze[agent[0]-1][agent[1]] = 3
        elif maze[agent[0]-1][agent[1]] == 2 or maze[agent[0]-1][agent[1]] == 4:
            count = 0
            y_to_look = np.array([agent[1]])
            y_to_move = [np.array([agent[1]])]
            move = True
            for j in range(agent[0]-1, -1, -1):
                all_zeros = True
                y_new = y_to_move[-1]
                for k in y_to_look:
                    if maze[j][k] == 2:
                        if maze[j+1][k] == 0: # might be a bug here
                            continue
                        all_zeros = False
                        if k+1 not in y_new:
                            y_new = np.append(y_new, k+1)
                            y_new = np.sort(y_new)
                        if k+1 not in y_to_look:
                            y_to_look = np.append(y_to_look, k+1)
                            y_to_look = np.sort(y_to_look)
                    elif maze[j][k] == 4:
                        if maze[j+1][k] == 0: # might be a bug here
                            continue
                        all_zeros = False
                        if k-1 not in y_new:
                            y_new = np.append(y_new, k-1)
                            y_new = np.sort(y_new)
                        if k-1 not in y_to_look:
                            y_to_look = np.append(y_to_look, k-1)
                            y_to_look = np.sort(y_to_look)
                    elif maze[j][k] == 1:
                        move = False
                        break
                if all_zeros:
                    break
                else:
                    count += 1
                y_to_move.append(y_new)
            if move:
                for j in range(count, 0, -1):
                    for k in y_to_look:
                        if maze[agent[0]-j][k] == 2:
                            maze[agent[0]-j-1][k] = 2
                            maze[agent[0]-j][k] = 0
                        elif maze[agent[0]-j][k] == 4:
                            maze[agent[0]-j-1][k] = 4
                            maze[agent[0]-j][k] = 0
                maze[agent[0]][agent[1]] = 0
                maze[agent[0]-1][agent[1]] = 3

    return maze

if __name__ == '__main__':
    with open("inputs/day15.txt") as f:
        data = f.read().splitlines()

    # data is seperated by one empty line
    data_1 = []
    data_2 = []
    for i in range(len(data)):
        if data[i] == "":
            data_2 = data[i+1:]
            break
        data_1.append(data[i])
        
    for i in range(len(data_1)):
        data_1[i] = [x for x in data_1[i].strip()]
    for i in range(len(data_2)):
        data_2[i] = [x for x in data_2[i].strip()]

    # concatenate the rows of data_2
    data_2 = [x for row in data_2 for x in row]

    # turn to numpy array of integers
    maze_init = np.zeros((len(data_1), len(data_1[0])), dtype=int)
    for i in range(len(data_1)):
        for j in range(len(data_1[0])):
            if data_1[i][j] == '#': # wall
                maze_init[i][j] = 1
            elif data_1[i][j] == 'O': # box
                maze_init[i][j] = 2
            elif data_1[i][j] == '@': # agent
                maze_init[i][j] = 3

    instructions = np.zeros(len(data_2), dtype=int)
    for i in range(len(data_2)):
        if data_2[i] == '>': # right
            instructions[i] = 0
        elif data_2[i] == 'v': # down
            instructions[i] = 1
        elif data_2[i] == '<': # left
            instructions[i] = 2
        elif data_2[i] == '^': # up
            instructions[i] = 3

    # Part 1 - Sum of all boxes' GPS coordinates

    # simulate the movement
    maze = maze_init.copy()
    for i, ins in enumerate(instructions):
        maze = move(maze, ins)

    # find the boxes
    boxes = np.where(maze == 2)
    
    # sum the boxes' GPS coordinates
    sum = 0
    for i in range(len(boxes[0])):
        sum += boxes[0][i]*100 + boxes[1][i]
    print(f'Sum of all boxes\' GPS coordinates: {sum}')

    # Part 2 - Twice as wide maze

    # double the width of the maze
    maze = np.zeros((len(maze_init), len(maze_init[0])*2), dtype=int)
    for i in range(len(maze_init)):
        for j in range(len(maze_init[0])):
            if maze_init[i][j] == 1:
                maze[i][j*2] = 1
                maze[i][j*2+1] = 1
            elif maze_init[i][j] == 2:
                maze[i][j*2] = 2
                maze[i][j*2+1] = 4
            elif maze_init[i][j] == 3:
                maze[i][j*2] = 3
                maze[i][j*2+1] = 0

    for i, ins in enumerate(instructions):
        maze = move_2(maze, ins)
        # only run this if you want to see the maze
        # render(maze, name=f'day15/{i}') # too many images, better save them to separate folder

    # find the boxes
    boxes = np.where(maze == 2) # only need to count the left side of the boxes
    # sum the boxes' GPS coordinates
    sum = 0
    for i in range(len(boxes[0])):
        sum += boxes[0][i]*100 + boxes[1][i]
    print(f'Sum of all boxes\' GPS coordinates in the twice as wide maze: {sum}')


