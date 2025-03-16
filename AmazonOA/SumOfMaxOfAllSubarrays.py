
from typing import List


# Warehouse has n products, i in products[] = amount of product i
# Ship products in batches, each batch has to have distinct items,
# each batch has to have more items than previous batch.

# How many batches can be shipped?

# 5, [2,3,1,4,2] -> 4
# 3, [1,2,7] -> 3

def sumOfMaxOfAllSubarrays(nums: List[int]) -> int:
    l = len(nums)
    left = [-1] * l
    right = [l] * l
    stk = []
    for i in range(l):
        while stk and nums[stk[-1]] < nums[i]:
            stk.pop()
        if stk:
            left[i] = stk[-1]
        stk.append(i)
    stk.clear()
    for i in range(l-1, -1, -1):
        while stk and nums[stk[-1]] <= nums[i]:
            stk.pop()
        if stk:
            right[i] = stk[-1]
        stk.append(i)
    mod = int(1e9)+7
    res = 0
    for i in range(l):
        temp = (i - left[i]) * (right[i] - i) % mod
        temp = (temp * (temp + 1)) / 2
        res += temp * nums[i] % mod
        res %= mod
    return int(res)

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(sumOfMaxOfAllSubarrays(nums))

if __name__ == "__main__":
    main()