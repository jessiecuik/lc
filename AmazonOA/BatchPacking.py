
from typing import List


# Warehouse has n products, i in products[] = amount of product i
# Ship products in batches, each batch has to have distinct items,
# each batch has to have more items than previous batch.

# How many batches can be shipped?

# 5, [2,3,1,4,2] -> 4
# 3, [1,2,7] -> 3

def maximizeGroups(products: List[int]) -> int:
    products.sort()
    count = idx = 0
    l = len(products)
    for i in range(1, l+1): 
        while products[idx] < i:
            idx += 1
            if idx == l: break
        count += 1
        idx += 1
        if idx == l: break
    return count

def main():
    n = int(input())
    products = []
    for i in range(n):
        products.append(int(input()))
    print(maximizeGroups(products))

if __name__ == "__main__":
    main()