def RunProgram(instructions, register_A=0, register_B=0, register_C=0, output=[]):
    '''
    Generator that runs the program and yields the output
    '''
    i = 0
    while i+1 < len(instructions):
        # check instruction[i+1] to see if it is a register or a value
        if instructions[i+1] == 4:
            combo = register_A
        elif instructions[i+1] == 5:
            combo = register_B
        elif instructions[i+1] == 6:
            combo = register_C
        elif instructions[i+1] == 7:
            combo = None
        else:
            combo = instructions[i+1]

        number = instructions[i+1]

        if instructions[i] == 0:
            out = register_A / 2**combo
            register_A = int(out)
        elif instructions[i] == 1:
            out = register_B ^ number
            register_B = out
        elif instructions[i] == 2:
            # modulo
            out = combo % 8
            register_B = out
        elif instructions[i] == 3:
            if register_A != 0:
                i = number - 2
        elif instructions[i] == 4:
            out = register_B ^ register_C
            register_B = out
        elif instructions[i] == 5:
            out = combo % 8
            output.append(out)
            yield out
        elif instructions[i] == 6:
            out = register_A / 2**combo
            register_B = int(out)
        elif instructions[i] == 7:
            out = register_A / 2**combo
            register_C = int(out)
        else:
            print("Invalid instruction")
            break
        i += 2

def Backtrack(instructions, output, prev_A=0):
    '''
    Backtrack to find the lowest A that produces the output
    '''
    if not output:
        return prev_A
    for register_A in range(1024):
        if register_A >> 3 == prev_A & 127 and next(RunProgram(instructions, register_A, 0, 0, [])) == output[-1]:
            ret = Backtrack(instructions, output[:-1], (prev_A << 3) | (register_A % 8))
            if ret is not None:
                return ret


if __name__ == "__main__":
    with open("inputs/day17.txt") as f:
        data = f.read().splitlines()

    register_A = int(data[0].split(': ')[1])
    register_B = int(data[1].split(': ')[1])
    register_C = int(data[2].split(': ')[1])

    instructions = data[4].split(': ')[1].split(',')
    instructions = [int(i) for i in instructions]

    # Part 1 - Output of the program

    output = list(RunProgram(instructions, register_A, register_B, register_C, []))
    print(f"Output: {','.join([str(i) for i in output])}")

    # Part 2 - Lowest Register A that produces an output which is the same as the instructions

    lowest_A = Backtrack(instructions, instructions)
    print(f"Lowest A: {lowest_A}")