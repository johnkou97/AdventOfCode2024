import numpy as np

def MixAndPrune(number: int, new_number: int) -> None:
    '''
    Mixes the number with the new number and prunes the result to 24 bits.
    '''
    number = number ^ new_number    # mix (XOR)
    number = number % 16777216      # prune (modulus)
    return number

def GenenerateSecretNumber(number: int) -> int:
    '''
    Generates the next secret number.
    Works like a pseudo-random number generator.
    '''
    new_number = 64 * number
    number = MixAndPrune(number, new_number)

    new_number = int(number/32)
    number = MixAndPrune(number, new_number)

    new_number = 2048 * number
    number = MixAndPrune(number, new_number)

    return number

def BuildSequences(price_diff: np.ndarray, price: np.ndarray) -> dict:
    '''
    Pre-compute a mapping of 4-tuples (price differences) to the total bananas they yield.
    For each row, we iterate over the price differences and the price of bananas.
    We create a 4-tuple key and sum up the price of bananas at the next index.
    We make sure to only add the value once per row.
    '''
    sequences = {}
    for i in range(len(price_diff)):  # Iterate over each row
        sequences_row = {} 
        for j in range(3, price_diff.shape[1]):  # Iterate over valid indices
            # Create the 4-tuple key
            key = tuple(price_diff[i, j-3:j+1])
            # Sum up the price of bananas at the next index
            value = price[i, j+1]
            if key not in sequences_row: # only add the value once per row
                sequences_row[key] = value
                sequences[key] = sequences.get(key, 0) + value

    return sequences

def FindBestSequence(sequences: dict) -> np.ndarray:
    '''
    Find the sequence that gives the maximum bananas.
    '''
    best_sequence = max(sequences, key=sequences.get)
    return np.array(best_sequence)


if __name__ == "__main__":
    with open("inputs/day22.txt") as f:
        data = f.read().splitlines()

    # turn data into a list of integers
    data = list(map(int, data))

    # Part 1 - Sum of the all the 200th Secret Numbers

    n = 2000  # number of secret numbers to generate

    secret_number = np.empty((len(data),n), dtype=int)  # this is too much for Part 1
                                                        # but it will come in handy for Part 2
    for i, number in enumerate(data):
        for j in range(n):
            number = GenenerateSecretNumber(number)
            secret_number[i][j] = number

    print(f"Sum of the 200th Secret Numbers: {np.sum(secret_number[:,-1])}")

    # Part 2 - Find the sequence that will get you the most bananas

    # get price of bananas (last digit of the secret number)
    price = secret_number % 10

    # get price difference between each pair of consecutive secret numbers
    price_diff = np.diff(price, axis=1)

    # build a dictionary of 4-tuples to the total bananas they yield
    sequences = BuildSequences(price_diff, price)

    # find the 4-tuple sequence that gives the maximum bananas
    best_sequence = FindBestSequence(sequences)
    print(f"Total number of bananas: {sequences[tuple(best_sequence)]}")

