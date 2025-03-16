from typing import List

# Given list of coins, replace denominations to get lesser number of coins.
# Find the smallest denomination with multiple coins.
# Replace 2 of the leftmost occurence of the smallest valued coins
# with a coin that is double it's value, placed at the right index of the 2 being replaced.
# Repeat till end and return final order of coins

# [3, 4, 1, 2, 2, 1, 1] => [3, 8, 2, 1]



def getFinalValues(coins: List[int]) -> List[int]:
    denominations = {}
    num_coins = len(coins)
    # have a mapping of denominations to their indices
    for i in range(num_coins):
        if coins[i] in denominations:
            denominations[coins[i]].append(i)
        else:
            denominations[coins[i]] = [i]
    # keep a sorted array of denominations
    sorted_denoms = sorted(denominations.keys())
    # going from smallest denom to largest, if there are 2+ of curr denom
    # replace with 2* curr denom
    for denom in sorted_denoms:
        while len(denominations[denom]) >= 2:
            # take left 2 occurences of curr denom out
            right_idx = denominations[denom][1]
            if len(denominations[denom]) == 2:
                del denominations[denom]
            else:
                denominations[denom] = denominations[denom][2:]
            # add new occurence of 2* curr denom
            if (denom * 2) in denominations:
                denominations[denom * 2].append(right_idx)
            else:
                denominations[denom * 2] = [right_idx]
                break
    # put remaining coins in order
    final_values = [0] * num_coins
    for denom, indices in denominations.items():
        for i in range(len(indices)):
            final_values[indices[i]] = denom
    final_values = [value for value in final_values if value != 0]
    return final_values

def main():
    num_coins = int(input())
    coins = []
    for i in range(num_coins):
        coins.append(int(input()))
    print("Final values are:", getFinalValues(coins))

if __name__ == "__main__":
    main()