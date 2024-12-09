def calculate_checksum(memory):
    checksum = 0
    for i,num in enumerate(memory):
        if num == -1:
            continue
        checksum += num * i
    return checksum

if __name__ == "__main__":
    import numpy as np

    with open("inputs/day9.txt") as f:
        data = f.read()
    
    data = list(data.strip())
    data = np.array(data, dtype=int)
    
    # create memory
    sum = np.sum(data)
    memory_init = np.full(sum, -1, dtype=int)
    id = 0
    pos = 0
    for i, digit in enumerate(data):
        if i % 2 == 0:
            memory_init[pos:pos+digit] = id
            id += 1
            pos += digit
        else:
            pos += digit

    # Part 1 - reaarange memory to free up space and calculate checksum

    # create copy of memory
    memory = memory_init.copy()

    # rearaange memory from right to left
    for i in range(len(memory)-1, 0, -1):
        if memory[i] != -1:
            # find from the left the first -1
            for j in range(i-1):
                if memory[j] == -1:
                    memory[j] = memory[i]
                    memory[i] = -1
                    break

    # calculate the checksum
    checksum = calculate_checksum(memory)
    print(f"Checksum: {checksum}")

    # Part 2 - reaarange memory by moving whole files and calculate checksum

    # create copy of memory
    memory = memory_init.copy()

    # rearaange memory from right to left by moving whole files
    prev = -69
    for i in range(len(memory)-1, 0, -1):
        if memory[i] == prev:
            continue
        prev = memory[i]
        if memory[i] != -1:
            # find how many same numbers are in a row
            j = i
            while memory[j] == memory[i]:
                j -= 1
            length = i - j 
            # find from the left the first space to move the whole file
            for j in range(i-1):
                if memory[j] == -1:
                    # check if there is enough space
                    if np.all(memory[j:j+length] == -1):
                        memory[j:j+length] = memory[i-length+1:i+1]
                        memory[i-length+1:i+1] = -1
                        break

    # calculate the checksum
    checksum = calculate_checksum(memory)
    print(f"Checksum when moving whole files: {checksum}")
