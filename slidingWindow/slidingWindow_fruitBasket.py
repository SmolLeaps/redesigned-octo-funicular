"""
Difficulty: Medium

Input: Fruit = ['A', 'B', 'C', 'A', 'C']
Output: 3, because we can put 2 'C' in 1 basket and 1 'A' in the other from the subarray ['C', 'A', 'C']
"""

def fruitsIntoBaskets(fruits):
    total_size = 0
    start = 0
    for end in range(1, len(fruits) + 1):
        curr_window = fruits[start:end]
        num_distinct_fruits = len(set(curr_window))
        while num_distinct_fruits > 2:
            start += 1
            curr_window = fruits[start:end]
            num_distinct_fruits = len(set(curr_window))
        total_size = max(total_size, len(curr_window))
    return total_size

fruitBasket1=['A', 'B', 'C', 'B', 'B', 'C']
fruitBasket1=['A', 'B', 'C', 'B', 'B', 'C', 'A']
print(fruitsIntoBaskets(fruitBasket1))