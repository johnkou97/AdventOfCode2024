if __name__ == '__main__':
    import numpy as np

    with open("inputs/day13.txt") as f:
        data = f.read().splitlines()

    coeff = []
    values = []
    for i in range(len(data)):
        if i % 4 == 0 or i % 4 == 1:
            coeff.append([int(data[i].split(",")[0].split(" ")[-1].split("X")[-1]), int(data[i].split(",")[1].split("Y")[-1])])
        elif i % 4 == 2:
            values.append([int(data[i].split(",")[0].split("=")[-1]), int(data[i].split(",")[1].split("=")[-1])])
    
    coeff = np.array(coeff)
    values = np.array(values)

    # Part 1 - Find the fewest tokens to spend to win all possible prizes
    
    # solve all systems of 2 equations
    solutions = []
    for i in range(len(values)):
        # solve the system 
        a = np.array([[coeff[2*i][0], coeff[2*i+1][0]], [coeff[2*i][1], coeff[2*i+1][1]]])
        b = np.array([values[i][0], values[i][1]])
        if np.linalg.det(a) != 0:
            solution = np.linalg.solve(a, b)
            # find if solution is integer, be forgiving with floating point errors
            if np.all(np.abs(np.round(solution) - solution) < 1e-4):
                solution = np.round(solution).astype(int)
            else:
                solution = [0, 0] # the solution is not [0, 0] but it works for this problem
            solutions.append(solution)
        else:
            solutions.append([0, 0]) # same as above

    # calculate total tokens spent
    total = 0
    for a, b in solutions:
        total += a*3 + b

    print(f"Total tokens spent: {total}")

    # Part 2 - Conversion error on positions, re-solve the system of equations
    error = 10000000000000

    # fix error in all values
    values = values + error

    # solve all systems of 2 equations
    solutions = []
    for i in range(len(values)):
        # solve the system 
        a = np.array([[coeff[2*i][0], coeff[2*i+1][0]], [coeff[2*i][1], coeff[2*i+1][1]]])
        b = np.array([values[i][0], values[i][1]])
        if np.linalg.det(a) != 0:
            solution = np.linalg.solve(a, b)
            # find if solution is integer, be forgiving with floating point errors
            if np.all(np.abs(np.round(solution) - solution) < 1e-4):
                solution = np.round(solution).astype(int)
            else:
                solution = [0, 0] # the solution is not [0, 0] but it works for this problem
            solutions.append(solution)
        else:
            solutions.append([0, 0]) # same as above

    # calculate total tokens spent
    total = 0
    for a, b in solutions:
        total += a*3 + b

    print(f"Total tokens spent after conversion error: {total}")