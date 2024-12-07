if __name__ == "__main__":
    import numpy as np

    with open("inputs/day7.txt") as f:
        data = f.read().splitlines()
        
    # take the result
    result = [x.split(":")[0] for x in data]
    result = np.array(result).astype(int)

    # keep the rest as a list of integers. There are multiple numbers separated by spaces
    numbers = [x.split(":")[1].split() for x in data]
    
    # convert the list of strings to a list of integers
    numbers = [list(map(int, x)) for x in numbers]

    # Part 1 - Find the sum of the results that can be generated from the numbers with addition or multiplication

    calibration_sum = 0
    for i in range(len(numbers)):
        loops = 2**(len(numbers[i])-1)
        for j in range(loops):
            temp = numbers[i][0]
            for k in range(len(numbers[i])-1):
                if (j // (2 ** k)) % 2 == 1:
                    temp += numbers[i][k+1]
                else:
                    temp *= numbers[i][k+1]
            if temp == result[i]:
                calibration_sum += temp
                break

    print("Calibration sum:", calibration_sum)

    # Part 2 - Find the sum of the results that can be generated from the numbers with addition or multiplication or concatenation

    new_calibration_sum = 0
    for i in range(len(numbers)):
        loops = 3**(len(numbers[i])-1)
        for j in range(loops):
            temp = numbers[i][0]
            for k in range(len(numbers[i])-1):
                if (j // (3 ** k)) % 3 == 0:
                    temp += numbers[i][k+1]
                elif (j // (3 ** k)) % 3 == 1:
                    temp *= numbers[i][k+1]
                else:
                    temp = int(str(temp) + str(numbers[i][k+1]))
            if temp == result[i]:
                new_calibration_sum += temp
                break

    print("New calibration sum:", new_calibration_sum)
