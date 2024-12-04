if __name__ == '__main__':
    import numpy as np

    with open('inputs/day4.txt') as f:
        lines = f.readlines()
    
    # convert the list of strings to numpy array
    lines = np.array([list(x.strip()) for x in lines])

    vertical, horizontal = lines.shape

    # Part 1 - find all XMAS 

    
    # search for XMAS
    xmas = 0
    for i in range(vertical):
        for j in range(horizontal-3):
            # horizontal
            if lines[i][j] == 'X' and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
                xmas += 1
            elif lines[i][j] == 'S' and lines[i][j+1] == 'A' and lines[i][j+2] == 'M' and lines[i][j+3] == 'X':
                xmas += 1
            
            # vertical
            if lines[j][i] == 'X' and lines[j+1][i] == 'M' and lines[j+2][i] == 'A' and lines[j+3][i] == 'S':
                xmas += 1
            elif lines[j][i] == 'S' and lines[j+1][i] == 'A' and lines[j+2][i] == 'M' and lines[j+3][i] == 'X':
                xmas += 1

            # diagonal
            if i < vertical-3:
                if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                    xmas += 1
                elif lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M' and lines[i+3][j+3] == 'X':
                    xmas += 1
                
                if lines[i][j+3] == 'X' and lines[i+1][j+2] == 'M' and lines[i+2][j+1] == 'A' and lines[i+3][j] == 'S':
                    xmas += 1
                elif lines[i][j+3] == 'S' and lines[i+1][j+2] == 'A' and lines[i+2][j+1] == 'M' and lines[i+3][j] == 'X':
                    xmas += 1



    print(f"Number of XMAS: {xmas}")

    # Part 2 - find all X-MAS

    # search for X-MAS
    x_mas = 0
    for i in range(horizontal-2):
        for j in range(vertical-2):
            if lines[i][j] == 'M' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'S':
                if lines[i][j+2] == 'M' and lines[i+1][j+1] == 'A' and lines[i+2][j] == 'S':
                    x_mas += 1
                elif lines[i][j+2] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j] == 'M':
                    x_mas += 1
            elif lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M':
                if lines[i][j+2] == 'M' and lines[i+1][j+1] == 'A' and lines[i+2][j] == 'S':
                    x_mas += 1
                elif lines[i][j+2] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j] == 'M':
                    x_mas += 1

    print(f"Number of X-MAS: {x_mas}")
            
