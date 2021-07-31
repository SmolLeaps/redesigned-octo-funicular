"""
Q2 - Fixed size sliding window
Find the max total of any contiguous subarray of size K.
Time complexity: O(n)
"""


def findMaximumtotalSubarray(array, k):
    total = sum(array[0:k]) 
    print("first total:", total)
    currentHighest = total
    for i in range(0, len(array)-k):
        total -= array[i]
        total += array[i+k]
        if(total>currentHighest):
            currentHighest = total
    return currentHighest

array = [2, 1, 5, 1, 3, 2]
k = 4
print(findMaximumtotalSubarray(array, k))
