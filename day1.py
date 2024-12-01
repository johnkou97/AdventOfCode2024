if __name__ == "__main__":
    import numpy as np

    list_1 = []
    list_2 = []

    # Read the data from the file
    with open("inputs/day1.txt") as file:
        for line in file:
            line = line.strip()
            a, b = line.split("   ")
            list_1.append(int(a))
            list_2.append(int(b))

    # Convert the lists to numpy arrays
    list_1 = np.array(list_1)
    list_2 = np.array(list_2)

    # Sort the arrays
    list_1.sort()
    list_2.sort()

    # Part 1 - Find the total distance between the two lists

    # Find the differences between the elements of the arrays
    diff = list_2 - list_1

    # take the absolute value of the differences
    diff = np.abs(diff)

    # Find the sum of the differences
    sum_diff = np.sum(diff)

    print(f"The total distance between the two lists is: {sum_diff}")

    # Part 2 - Find the similarity score between the two lists

    score = 0
    for element in list_1:
        # count how many times the element appears in list_2 
        count = np.count_nonzero(list_2 == element)
        # add the count to the score
        score += count*element

    print(f"The similarity score between the two lists is: {score}")
