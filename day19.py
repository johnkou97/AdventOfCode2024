import numpy as np

def MatchPattern(pattern: np.array, display: str, memo: dict = {}) -> int:
    '''
    Recursive function to match the pattern with the display
    Using memoization to store the results of the subproblems
    Counts how many different ways the pattern can be matched
    '''
    if display in memo:
        return memo[display]
    
    # Base case: if the display is empty, the pattern matches
    if len(display) == 0:
        # memo[display] = 1  # no need to memoize this since we are not going to use it
                             # but might be useful for other purposes, like sharing the
                             # memo dictionary across multiple calls
        return 1
    
    # Recursive case: try matching each pattern at the start of the display
    count = 0
    for p in pattern:
        if display.startswith(p):
            count += MatchPattern(pattern, display[len(p):], memo)

    # memoize and return the count
    memo[display] = count
    return count


if __name__ == "__main__":
    with open("inputs/day19.txt") as f:
        data = f.read().splitlines()

    # load the patterns
    patterns = data[0].split(", ")
    patterns = np.array(patterns)

    onsen_display = data[2:]
    onsen_display = np.array(onsen_display)

    count = 0
    count_total = 0
    for i, display in enumerate(onsen_display):
        match = MatchPattern(patterns, display)
        count_total += match
        if match > 0:
            count += 1

    print(f"Number of displays that can be matched: {count}")
    print(f"Total number of ways the pattern can be matched: {count_total}")