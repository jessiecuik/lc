from typing import Counter, List

def getMaxIncrements(ratings: List[int]) -> int:
    count = 0
    elements = Counter(ratings)
    counts = list(elements.values()).sort()
    num_elements = len(counts)
    for i in range(num_elements-1):
        count += min(counts[i],counts[i+1])
    return count

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(getMaxIncrements(nums))

if __name__ == "__main__":
    main()