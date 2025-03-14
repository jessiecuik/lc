from typing import List


# n customers
# initialRewards[i] = ith customer's points so far
# winner += n points
# second place += n-1 points
# ... last place += 1 point

# find number of customers that will have highest points if they win the final tournament
# countPossibleWinners(n:int, initialRewards: List[int]) -> int

# 3, [1,3,4] -> 2
# 4, [5,7,9,11] -> 1
# 3, [10,9] -> 2

def countPossibleWinners(n: int, initialRewards: List[int]) -> int:
    highest = max(initialRewards)
    count = 0
    for i in range(n):
        endingPoints = initialRewards[i] + n #points of i if won
        if endingPoints >= highest + n - 1:
            count += 1
    return count

def main():
    n = int(input())
    initialRewards = []
    for i in range(n):
        initialRewards.append(int(input()))
    print(countPossibleWinners(n, initialRewards))

if __name__ == "__main__":
    main()