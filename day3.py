if __name__ == "__main__":
    import numpy as np

    with open('inputs/day3.txt') as f:
        lines = f.readlines()
    
    # Part 1 - uncorrupt multiplication of numbers

    sum = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        # go by each element in the line
        for j in range(len(line)):
            # check if the elements are 'mul('
            if line[j:j+4] == 'mul(':
                # find the closing bracket
                for k in range(j+3, j+12):
                    if line[k] == ')':
                        # extract the numbers separated by ','
                        try:
                            numbers = line[j+4:k].split(',')
                            # convert to integers
                            numbers = [int(x) for x in numbers]
                            # multiply the numbers
                            product = np.prod(numbers)
                            # add to sum
                            sum += product
                            break
                        except:
                            break

    print(f"Sum of all products: {sum}")

    # Part 2 - take into account do and don't multiply

    sum = 0
    do = True
    for i in range(len(lines)):
        line = lines[i].strip()
        # go by each element in the line
        for j in range(len(line)):
            # check if the elements are 'do()' or 'don't()'
            if line[j:j+4] == 'do()':
                do = True
            elif line[j:j+7] == "don't()":
                do = False
            # check if the elements are 'mul('
            if line[j:j+4] == 'mul(' and do:
                # find the closing bracket
                for k in range(j+3, j+12):
                    if line[k] == ')':
                        # extract the numbers separated by ','
                        try:
                            numbers = line[j+4:k].split(',')
                            # convert to integers
                            numbers = [int(x) for x in numbers]
                            # multiply the numbers
                            product = np.prod(numbers)
                            # add to sum
                            sum += product
                            break
                        except:
                            break

    print(f"Sum of all products with do and don't in mind: {sum}")