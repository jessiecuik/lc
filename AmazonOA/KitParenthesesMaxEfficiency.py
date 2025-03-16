from typing import List

# "Parentheses Perfection Kit." - contains different types of parentheses, each with a specific efficiency rating.
# Create a balanced sequence of parentheses by adding zero or more parentheses from the kit to maximize total EfficiencyScore.
# EfficiencyScore = sum of the efficiency ratings of parentheses used from the kit.
# A sequence needs to be balanced = equal number of opening '(' and closing )' parentheses, in correct order.
# Given initial parentheses sequence input_string, kit_parentheses, and their respective efficiency ratings efficiency_ratings.
# EfficiencyScore of original string = 0. You can use any number of unused parentheses from the kit.
# Determine the maximum possible EfficiencyScore that can be achieved for the resulting balanced sequence.
# It is guaranteed that the sequence can be made balanced by adding zero or more parentheses from the kit.

# input_string = ")(("
# kit_parentheses = ")(()))"
# efficiency_ratings = [3, 4, 2, -4, -1, -3]
# => 6 

# input_string = "()"
# kit_parentheses = "(())"
# efficiency_ratings = [4, 2, -3, -3]
# => 1

def maximizeEfficiencyScore(input_string: str, kit_parentheses: str, efficiency_ratings: List[int]) -> int:
    # check if input is balanced
    l = len(input_string)
    stk = []
    left_needed = 0
    right_needed = 0
    for i in range(l):
      if input_string[i] == '(':
        stk.append(input_string[i])
      elif stk:
        stk.pop()
      else:
        left_needed += 1
    right_needed = len(stk)
    # create value lists for both brackets
    left_values = []
    right_values = []
    kit_size = len(kit_parentheses)
    for i in range(kit_size):
      if kit_parentheses[i] == '(':
        left_values.append(efficiency_ratings[i])
      else:
        right_values.append(efficiency_ratings[i])
    left_values.sort(reverse=True)
    right_values.sort(reverse=True)
    # if not balanced, look for max efficiency required to make balanced
    max_efficiency = 0
    if left_needed > 0:
      max_efficiency += sum(left_values[:left_needed])
      left_values = left_values[left_needed:]
    if right_needed > 0:
      max_efficiency += sum(right_values[:right_needed])
      right_values = right_values[right_needed:]
    # if balanced, check for positive parentheses pairs
    while left_values and right_values and (left_values[0] + right_values[0] > 0):
      max_efficiency += left_values[0] + right_values[0]
      del left_values[0], right_values[0]
    return max_efficiency

def main():
    input_string = input()
    kit_parentheses = input()
    kit_size = len(kit_parentheses)
    efficiency_ratings = []
    for n in range(kit_size):
        efficiency_ratings.append(int(input()))
    print(maximizeEfficiencyScore(input_string, kit_parentheses, efficiency_ratings))

if __name__ == '__main__':
    main()