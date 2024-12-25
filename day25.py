# ------- Final Day -------
if __name__ == "__main__":
    with open("inputs/day25.txt") as f:
        data = f.read().splitlines()

    keys = []
    locks = []
    for i in range(0, len(data), 8):
        heights = [0, 0, 0, 0, 0]
        for j in range(5):
            for k in range(1, 6):
                if data[i+k][j] == "#":
                    heights[j] += 1
        if data[i] == "#####":
            locks.append(heights)
        else:
            keys.append(heights)

    # Part 1 - Unique pairs of keys and locks that fit

    # find all the possible combinations of keys and locks that actually fit
    # a key fits a lock if the sum of the heights of the key and lock in each column is less than or equal to 5
    fits = 0
    for key in keys:
        for lock in locks:
            if all([key[i] + lock[i] <= 5 for i in range(5)]):
                fits += 1

    print(f'Number of fits: {fits}')

    # Part 2 - No code to write, just a Merry Christmas message

    # Merry Christmas! 
    # 🎄🎅🎁🎉🎊🎈🦌🔔🕯️🎶🍪🥛

    print("Merry Christmas!")


