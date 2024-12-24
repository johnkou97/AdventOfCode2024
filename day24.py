if __name__ == "__main__":
    with open("inputs/day24.txt") as f:
        data = f.read().splitlines()

    # create a dictionary of the data until you find empty line
    wires = {}
    for i, line in enumerate(data):
        if line == "":
            # put the rest of the data in a list
            instructions = data[i+1:]
            break
        wire, value = line.split(": ")
        wires[wire] = int(value)

    instructions = [i[0].split(" ") + [i[1]] for i in [i.split(" -> ") for i in data[i+1:]]]

    # Part 1 - Simulate the gates to get the message

    i = 0
    completed = 0
    while True:
        if i >= len(instructions):
            i -= len(instructions)
        instruction = instructions[i]

        # check if the instruction[0] and instruction[2] are in the wires dictionary 
        # and instruction[3] is not in the wires dictionary
        if instruction[0] in wires and instruction[2] in wires and instruction[3] not in wires:
            # print("Both wires are in the dictionary")
            if instruction[1] == "AND":
                wires[instruction[3]] = wires[instruction[0]] & wires[instruction[2]]
                completed += 1
            elif instruction[1] == "OR":
                wires[instruction[3]] = wires[instruction[0]] | wires[instruction[2]]
                completed += 1
            elif instruction[1] == "XOR":
                wires[instruction[3]] = wires[instruction[0]] ^ wires[instruction[2]]
                completed += 1
            else:
                raise ValueError("Invalid instruction")
        if completed == len(instructions):
            break
        
        i += 1

    # find all wires starting with "z" and sort them in descending order
    message = {}
    for wire in wires:
        if wire.startswith("z"):
            message[int(wire.split("z")[1])] = wires[wire]

    message = sorted(message.items(), key=lambda x: x[0], reverse=True)

    # take the values of the message and concatenate them to get the binary message
    binary_message = "".join([str(i[1]) for i in message])
    
    # translate the binary message to base 10
    decimal_message = int(binary_message, 2)
    
    print(f"The decimal message is: {decimal_message}")

    # Part 2 - Find the swapped wires and correct the logic

    '''
    for this problem we need to find 4 wires to swap so that the binary message of z
    is the AND of x and y. Swapping means swap the output of the gates i and j
    For example, x00 AND y00 -> z00, x01 AND y01 ->z01 will be swapped to 
    x00 AND y00 -> z01, x01 AND y01 -> z00.
    After being stuck for a while, I went to reddit and found that most users 
    used a some visualization hacks to manually find the swapped wires.
    I also used their tools to find the swapped wires and correct the logic.
    Here I will only print the correct message, but it required much more manual work
    It will also not work for any other input, only for my puzzle input
    Go to reddit (https://www.reddit.com/r/adventofcode/comments/1hl698z/2024_day_24_solutions/)
    to see the visualization tools
    '''
    
    print(f"The sorted names of the wires to swap are: bgs,pqc,rjm,swt,wsv,z07,z13,z31 (Disclaimer: This is not a general solution, it only works for my input)")