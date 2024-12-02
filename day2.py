import numpy as np

def check_valid_report(line):
    # check if all elements are either increasing (between 1 and 3) or decreasing (between -1 and -3)
    if np.all(np.diff(line) >= 1):
        if np.all(np.diff(line) <= 3):
            return True
    elif np.all(np.diff(line) <= -1):
        if np.all(np.diff(line) >= -3):
            return True
    return False

if __name__ == "__main__":
    # get number of lines in file
    with open('inputs/day2.txt') as f:
        lines = f.readlines()

    # Part 1 - find number of valid reports

    counter = 0
    for i in range(len(lines)):
        # read each line 
        line = lines[i].strip().split(' ')
        # convert to integers and store in array
        line = np.array([int(x) for x in line])
        # check validity of report
        if check_valid_report(line):
            counter += 1

    print(f"Number of valid reports: {counter}")

    # Part 2 - find number of valid reports with Problem Dampener

    counter = 0
    for i in range(len(lines)):
        # read each line 
        line = lines[i].strip().split(' ')
        # convert to integers and store in array
        line = np.array([int(x) for x in line])
        # check validity of report
        if check_valid_report(line):
            counter += 1
        else:
            for j in range(len(line)):
                new_line = np.delete(line, j)
                # check validity of report
                if check_valid_report(new_line):
                    counter += 1
                    break

    print(f"Number of valid reports with Problem Dampener: {counter}")