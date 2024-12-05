if __name__ == "__main__":
    import numpy as np

    with open("inputs/day5.txt") as f:
        data = f.read().splitlines()
        # find line which is empty
        for i, line in enumerate(data):
            if line == "":
                break
        data1 = data[:i]
        data2 = data[i+1:]

    x = []
    y = []
    for line in data1:
        x.append(int(line.split("|")[0]))
        y.append(int(line.split("|")[1]))

    x = np.array(x)
    y = np.array(y)

    # print(x)
    # print(y)

    # Part 1 - find the sum of the middle elements of correct orders

    sum_correct = 0
    not_correct = []
    for i in range(len(data2)):
        # comma separated values
        order = data2[i].split(",")
        # convert to numpy array of integers
        order = np.array(list(map(int, order)))
        
        order_flag = True
        for j in range(len(order)):
            # find if the order is in x and where (multiple values can be found)
            index = np.where(x == order[j])[0]
            # check if all previous elements are not in y and y is not empty
            if np.any(np.isin(order[:j], y[index])) and len(y[index]) > 0 and len(order[:j]) > 0:
                order_flag = False
                not_correct.append(i) # useful for part 2
                break
        
        if order_flag:
            # add the middle element to the sum
            sum_correct += order[len(order)//2]
        
    print(f"Sum correct: {sum_correct}")

    # Part 2 - correct the order of the non correct orders and find the sum of the middle elements

    sum_incorrect = 0
    for i in not_correct:
        # comma separated values
        order = data2[i].split(",")
        # convert to numpy array of integers
        order = np.array(list(map(int, order)))
        # print(order)
        
        for j in range(len(order)):
            # like in part 1
            index = np.where(x == order[j])[0]
            if np.any(np.isin(order[:j], y[index])) and len(y[index]) > 0 and len(order[:j]) > 0:
                # now correct the order
                # find the first element in order[:j] that is in y[index]
                k = np.where(np.isin(order[:j], y[index]))[0][0]
                # correct the order by putting order[j] before order[k] and removing order[j]
                order = np.insert(order, k, order[j])
                order = np.delete(order, j+1)

        # add the middle element to the sum
        sum_incorrect += order[len(order)//2]

    print(f"Sum incorrect: {sum_incorrect}")