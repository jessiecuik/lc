
from typing import List


# Warehouse has n products, i in products[] = amount of product i
# Ship products in batches, each batch has to have distinct items,
# each batch has to have more items than previous batch.

# How many batches can be shipped?

# 5, [2,3,1,4,2] -> 4
# 3, [1,2,7] -> 3

def sumOfMaxOfAllSubarrays(arr):
    n = len(arr)
    
    # Arrays to store contribution counts
    left = [0] * n
    right = [0] * n
    
    # Monotonic increasing stack (for left counts)
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    
    # Monotonic increasing stack (for right counts)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)
    
    # Compute the sum of contributions
    result = 0
    for i in range(n):
        result += arr[i] * left[i] * right[i]
    
    return result

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(sumOfMaxOfAllSubarrays(nums))

if __name__ == "__main__":
    main()