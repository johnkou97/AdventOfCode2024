from collections import deque
from functools import lru_cache

NUMERIC_KEYPAD = {
'A': ['0', '3'], '0': ['2', 'A'],
'1': ['4', '2'], '2': ['0', '1', '5', '3'],
'3': ['A', '2', '6'], '4': ['7', '5', '1'],
'5': ['2', '4', '8', '6'], '6': ['3', '5', '9'],
'7': ['4', '8'], '8': ['5', '7', '9'],
'9': ['6', '8']
}

DIRECTIONAL_KEYPAD = {
'>': ['v', 'A'], 'v': ['>', '<', '^'],
'<': ['v'], '^': ['v', 'A'], 'A': ['^', '>']
}

def NumericDirection(start: str, end: str) -> str:
    '''
    Determine the direction for moving from start to end on the numeric keypad.
    '''
    directions = {
        ('A', '0'): '<', ('A', '3'): '^',
        ('0', '2'): '^', ('0', 'A'): '>',
        ('1', '4'): '^', ('1', '2'): '>',
        ('2', '0'): 'v', ('2', '1'): '<', ('2', '3'): '>', ('2', '5'): '^',
        ('3', 'A'): 'v', ('3', '2'): '<', ('3', '6'): '^',
        ('4', '7'): '^', ('4', '1'): 'v', ('4', '5'): '>',
        ('5', '4'): '<', ('5', '2'): 'v', ('5', '6'): '>', ('5', '8'): '^',
        ('6', '3'): 'v', ('6', '5'): '<', ('6', '9'): '^',
        ('7', '4'): 'v', ('7', '8'): '>',
        ('8', '5'): 'v', ('8', '7'): '<', ('8', '9'): '>',
        ('9', '6'): 'v', ('9', '8'): '<'
    }
    return directions.get((start, end), '?')

def DirectionalDirection(start: str, end: str) -> str:
    '''
    Determine the direction for moving from start to end on the directional keypad.
    '''
    directions = {
        ('>', 'v'): '<', ('>', 'A'): '^',
        ('v', '>'): '>', ('v', '<'): '<', ('v', '^'): '^',
        ('<', 'v'): '>', ('^', 'v'): 'v', ('^', 'A'): '>',
        ('A', '^'): '<', ('A', '>'): 'v'
    }
    return directions.get((start, end), '?')

def BFSPath(start, target, type="numeric") -> list:
    '''
    Find all shortest paths between two points on a keypad.
    '''
    keypad = NUMERIC_KEYPAD if type == "numeric" else DIRECTIONAL_KEYPAD

    if start == target:
        return [[]]  # no moves required

    queue = deque([(start, [])])  # (current_position, path)
    visited = {}
    shortest_paths = []
    shortest_length = float('inf')

    while queue:
        position, path = queue.popleft()

        # if we find paths longer than the shortest, skip them
        if len(path) > shortest_length:
            continue

        # check if we have already visited this position with a shorter path
        if position in visited and len(path) > visited[position]:
            continue
        visited[position] = len(path)

        if position == target:
            # check if it's the shortest path found so far
            if len(path) < shortest_length:
                shortest_paths = [path]  # reset with this new shortest path
                shortest_length = len(path)
            elif len(path) == shortest_length:
                shortest_paths.append(path)  # add to the list of shortest paths
            continue

        # add neighbors to the queue
        for neighbor in keypad.get(position, []):
            queue.append((neighbor, path + [neighbor]))

    if not shortest_paths:
        raise ValueError(f"No valid path from {start} to {target}")

    return shortest_paths

@lru_cache(None)
def CachedBFSPath(start: str, target: str, type: str) -> list:
    '''
    Find all shortest paths between two points on a keypad.
    '''
    return BFSPath(start, target, type)

def ButtonSequences(code: str, type: str) -> list:
    '''
    Calculate all possible button press sequences for a single code on the numeric keypad.
    '''
    def generate_sequences(current_position, remaining_code):
        if not remaining_code:
            return [""]  # no more digits to process, return an empty sequence

        digit = remaining_code[0]
        next_digits = remaining_code[1:]

        # Get all shortest paths from current_position to digit
        # paths = BFSPath(current_position, digit, type)
        paths = CachedBFSPath(current_position, digit, type)
        all_sequences = []

        # process each path
        for path in paths:
            # translate the path into directional moves
            sequence_parts = []
            temp_position = current_position
            for step in path:
                if type == "numeric":
                    direction = NumericDirection(temp_position, step)
                elif type == "directional":
                    direction = DirectionalDirection(temp_position, step)
                sequence_parts.append(direction)
                temp_position = step

            # add the "A" for pressing the button
            sequence_parts.append("A")

            # recur for the remaining code
            suffixes = generate_sequences(temp_position, next_digits)
            for suffix in suffixes:
                all_sequences.append("".join(sequence_parts) + suffix)

        return all_sequences

    # start recursive sequence generation
    return generate_sequences('A', code)

def Robot(button_sequences: list) -> list:
    '''
    Calculate the shortest button press sequences for a robot to follow.
    '''
    # keep track of the lowest length sequences
    shortest_length = int(1e69) # arbitrarily large number
    shortest_sequences = []

    for button_sequence in button_sequences:
        directional_sequences = ButtonSequences(button_sequence, type="directional")
        for directional_sequence in directional_sequences:
            if len(directional_sequence) < shortest_length:
                shortest_length = len(directional_sequence)
                shortest_sequences = [directional_sequence]
            elif len(directional_sequence) == shortest_length:
                shortest_sequences.append(directional_sequence)

    return shortest_sequences

def CalculateComplexity(code: str, n_robots: int = 3) -> int:
    '''
    Calculate the complexity of a single code.
    '''
    sequences = ButtonSequences(code, type="numeric") # first robot, on the numeric keypad

    for _ in range(n_robots-1): # discount the first robot, which is on the numeric keypad
        sequences = Robot(sequences)

    length = len(sequences[0])
    numeric_part = int(code[:-1])  # remove trailing 'A'
    complexity = length * numeric_part

    return complexity


if __name__ == "__main__":
    with open("inputs/day21.txt") as f:
        data = f.read().splitlines()

    # Part 1 - Sum of complexity for 3 robots

    n_robots = 3
    total_complexity = 0
    for code in data: 
        complexity = CalculateComplexity(code, n_robots)
        total_complexity += complexity

    print(f"Total Complexity: {total_complexity}")

    # Part 2 - Sum of complexity for 25 robots
    # This is too slow to run in a reasonable amount of time
    # Need to find a more efficient way to calculate the complexity

    # n_robots = 25
    # total_complexity = 0
    # for code in data: 
    #     complexity = CalculateComplexity(code, n_robots)
    #     total_complexity += complexity

    # print(f"Total Complexity for {n_robots} robots: {total_complexity}")