from typing import List

# In Amazon's logistics network, n warehouses, 1 to n.
# Each has a storage capacity, warehouse[i].
# These warehouses are in non-decreasing order of their storage capacities
# Each warehouse has a connection to a distribution hub positioned at a location greater than or equal to its own.
# This means that a warehouse at position/can only connect to a hub at position j, where j >= i.
# The last warehouse has a central high-capacity distribution hub, at n.
# This hub = main connection point for all warehouses if necessary.
# The cost of establishing a connection from warehouse at i to a hub at position j = warehouseCapacity[j] - warehouseCapacity[i].
# Given queries of form (hubA, hubB), where two additional high-performance distribution hubs are added.
# Calculate the new minimum total connection cost for all warehouses.
# The problem statement assumes 1-based indexing for the warehouses array.
# •⁠ ⁠Each query is independent, i.e., the changes made do not persist for subsequent queries.

# warehouses = [0, 2, 5, 9, 12, 18]
# queries = [[2, 5], [1, 3]]
# => [12, 18]

# warehouses = [2, 6, 8, 14]
# queries = [[1, 2]]
# => [6]

# warehouses = [3, 6, 10, 15, 20]
# queries = [[2, 4]]
# => [8]


def getMinConnectionCost(warehouses: List[int], queries: List[List[int]]) -> List[int]:
    # calculate original total connection costs
    num_warehouses = len(warehouses)
    total_cost = 0
    new_costs = []
    for i in range(num_warehouses-1):
        total_cost += warehouses[-1] - warehouses[i]
    # for each query, calculate original connection costs for new hub warehouses
    for query in queries:
        hubA, hubB = query[0], query[1]
        orig_A_cost = warehouses[-1] - warehouses[hubA]
        orig_B_cost = warehouses[-1] - warehouses[hubB]
        # calculate hubA cost savings = (# hubs up to and including hubA) * original cost at hubA warehouse
        hubA_savings = (hubA + 1) * orig_A_cost
        # calculate hubB cost savings = (# hubs after hubA up to and including hubB) * original cost at hubB warehouse
        hubB_savings = (hubB - hubA) * orig_B_cost
        # total new connection costs = original cost - hubA savings - hubB savings
        new_costs.append(total_cost - hubA_savings - hubB_savings)
    return new_costs

def main():
    num_warehouses = int(input())
    warehouses = []
    for i in range(num_warehouses):
        warehouses.append(int(input()))
    num_queries = int(input())
    queries = []
    for i in range(num_queries):
        hubA = int(input()) - 1
        hubB = int(input()) - 1
        queries.append([hubA, hubB])
    connection_cost = getMinConnectionCost(warehouses, queries)
    print("Total connection cost is: ", connection_cost)

if __name__ == '__main__':
    main()