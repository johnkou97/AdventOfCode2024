import numpy as np

def entropy_calc(img):
    '''
    Calculate the entropy of an image
    Code from: https://stackoverflow.com/questions/50313114/what-is-the-entropy-of-an-image-and-how-is-it-calculated
    '''
    marg = np.histogramdd(np.ravel(img), bins = 256)[0]/img.size
    marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    entropy = -np.sum(np.multiply(marg, np.log2(marg)))
    return entropy


if __name__ == '__main__':
    with open("inputs/day14.txt") as f:
        data = f.read().splitlines()

    guards_init = []
    for line in data:
        x = line.split(",")[0].split("=")[1]
        y = line.split(",")[1].split(" ")[0]
        v_x = line.split("v=")[1].split(",")[0]
        v_y = line.split(",")[-1]
        guards_init.append([int(x), int(y), int(v_x), int(v_y)])

    guards_init = np.array(guards_init)

    guards = guards_init.copy()
    
    # Part 1 - Find the safety factor

    # simulate the guards
    seconds = 100
    for _ in range(seconds):
        guards[:,0] += guards[:,2]
        guards[:,1] += guards[:,3]

    # take into account the size of the grid
    width = 101
    height = 103
    guards[:,0] = guards[:,0] % width
    guards[:,1] = guards[:,1] % height

    # find how many guards are in each quadrant
    quadrant_1 = np.sum((guards[:,0] < int(width/2)) & (guards[:,1] < int(height/2)))
    quadrant_2 = np.sum((guards[:,0] < int(width/2)) & (guards[:,1] > int(height/2)))
    quadrant_3 = np.sum((guards[:,0] > int(width/2)) & (guards[:,1] < int(height/2)))
    quadrant_4 = np.sum((guards[:,0] > int(width/2)) & (guards[:,1] > int(height/2)))

    safety_factor = quadrant_1*quadrant_2*quadrant_3*quadrant_4
    print(f"Safety factor: {safety_factor}")

    # Part 2 - Christmas tree easter egg

    # simulate the guards
    guards = guards_init.copy()
    seconds = width*height # maximum number of seconds
    safety_factor = 1e69 # put a high value for the safety factor
    min_safe = 0
    all_safe = []
    img = None
    entropy = 1e69 # put a high value for the entropy
    min_seconds = 0
    all_entropy = []
    for i in range(seconds):
        guards[:,0] += guards[:,2]
        guards[:,1] += guards[:,3]

        # take into account the size of the grid
        guards[:,0] = guards[:,0] % width
        guards[:,1] = guards[:,1] % height

        # find how many guards are in each quadrant
        quadrant_1 = np.sum((guards[:,0] < int(width/2)) & (guards[:,1] < int(height/2)))
        quadrant_2 = np.sum((guards[:,0] < int(width/2)) & (guards[:,1] > int(height/2)))
        quadrant_3 = np.sum((guards[:,0] > int(width/2)) & (guards[:,1] < int(height/2)))
        quadrant_4 = np.sum((guards[:,0] > int(width/2)) & (guards[:,1] > int(height/2)))

        # First Approach: safety factor

        safe = quadrant_1*quadrant_2*quadrant_3*quadrant_4
        all_safe.append(safe) # keep track of all safety factors. Not necessary, just for plotting
        # if the safety factor is decreasing, keep track of the minimum
        if safe < safety_factor:
            safety_factor = quadrant_1*quadrant_2*quadrant_3*quadrant_4
            min_safe = i

        # create grid
        grid = np.zeros((height, width),dtype=int)
        for guard in guards:
            x = guard[0]
            y = guard[1]
            grid[y,x] += 1
        
        # Second Approach: entropy

        ent = entropy_calc(grid)
        all_entropy.append(ent) # keep track of all entropies. Not necessary, just for plotting
        # if the entropy is decreasing, keep track of the minimum
        if ent < entropy:
            entropy = ent
            min_seconds = i
            img = grid.copy()   # keep track of the image where the message is visible
                                # Not necessary, just for plotting the christmas tree
            

    # make sure both approaches find the same result
    print(f"Both approaches find the same result: {min_seconds == min_safe}")
    if min_seconds == min_safe:
        print(f"Easter egg is visible at {min_seconds+1} seconds with entropy {entropy} and safety factor {safety_factor}")
    else:
        print(f"Approach 1 using safety factor: Easter egg should be visible at {min_safe+1} seconds with safety factor {safety_factor}")
        print(f"Approach 2 using entropy: Easter egg should be visible at {min_seconds+1} seconds with entropy {entropy}")

    # Plotting. Not necessary, just for fun. Requires matplotlib.
    import matplotlib.pyplot as plt
    # create image
    plt.figure(figsize=(10,10))
    plt.imshow(img, cmap="hot")
    plt.savefig("outputs/day14_easter_egg.png")
    plt.close()

    # plot safety factor
    plt.figure(figsize=(10,10))
    plt.scatter(range(len(all_safe)), all_safe)
    # mark the point where the message is visible
    plt.scatter(min_safe, all_safe[min_safe], color="red")
    plt.savefig("outputs/day14_safety_factor.png")
    plt.close()

    # plot entropy
    plt.figure(figsize=(10,10))
    plt.scatter(range(len(all_entropy)), all_entropy)
    # mark the point where the message is visible
    plt.scatter(min_seconds, all_entropy[min_seconds], color="red")
    plt.savefig("outputs/day14_entropy.png")
    plt.close()
