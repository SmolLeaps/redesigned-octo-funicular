"""
Q3 - Variable size sliding window
Find the smallest subarray of any contiguous subarray of at least given sum S.
Time complexity: O(n)

EDGE CASES:
- The smallest subarray is size 1 (there is an element in the array that is larger or equals to S).
- All the elements in the array does not sum up to S.

2 repetitive motions: 
1. keep moving RIGHT pointer to the right to compare if sum exceeds S
2. the moment we hit equals to or above S, we want to move the LEFT pointer so that we can try to get the smallest subarray

[1, 3, 8], S=7

[1], S=1
> increase right pointer
[1, 3], S=4
> increase right pointer
[1, 3, 8], S=12
> increase left pointer
[3, 8], S=11 (keep going on because S >= 7)
> increase left pointer again
[8], S=8

Changing window size: start from first element, slowly expand window size 1,2,3. 
Stop when window size gives sum greater or equal to some condition, S. 
Note down the consituents of this window that satisfied the condition.
"""

def findSmallestSubarray(array, S):
    #we are varying the window size because we want to 
    smallest_window_size = float('inf')
    left_ptr = right_ptr = 0
    window_sum = array[0]
    while (right_ptr < len(array)-1):
        while (window_sum<=S) and (right_ptr<len(array)-1): #expands window from the right when sum < S
            right_ptr += 1
            window_sum += array[right_ptr]
            print("1st while loop",window_sum, " rightptr: ", right_ptr)
        while (window_sum>S) and ((right_ptr - left_ptr + 1) > 1): #shrinks window from the left when sum > S
            current_window_size = right_ptr - left_ptr + 1
            if (current_window_size < smallest_window_size):
                smallest_window_size = current_window_size 
                print("==>window size",smallest_window_size, " elements: ", array[left_ptr:right_ptr])
            window_sum -= array[left_ptr]
            left_ptr += 1
            print("2nd while loop", window_sum, " rightptr: ", right_ptr)
        # if (smallest_window_size == 1 and window_sum>S):
        #     return smallest_window_size

    if smallest_window_size == float('inf'):
        return 0
    else:
        return smallest_window_size

# def findSmallestSubarray(array, S):
#     window_sum = 0
#     min_length = float('inf')
#     window_start = 0
#     for window_end in range(len(array)):
#         window_sum += array[window_end]

#         while window_sum >= S:
#             current_length = window_end - window_start + 1
#             if current_length < min_length:
#                 min_length = current_length

#             window_sum -= array[window_start]
#             window_start += 1

#     if min_length == float('inf'):
#         return 0
#     else:
#         return min_length

testcase1 = [2, 1, 7, 2, 3, 2]
testcase2 = [1,1,1,1,1,1,1]
S = 8
print(findSmallestSubarray(testcase1, S))
