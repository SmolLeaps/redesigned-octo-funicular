'''
Q1 - Fixed size sliding window
Getting the average of Size K contiguous subarrays in an array
Time Complexity: O(n)

- iterate through a given list
- in each iteration, minus the "first", eg. array[i], plus the i+4 th element
'''

def slidingWindow_sizeKsubarray(k, array):
    # traversing through the array
    total = sum(array[0:k])
    averages = [total/k] #stores the moving average result calculated through the traversal. 
    for i in range(0, len(array) - k):
        #slide the window to the right, traverse the array
    
        # base case: 0 1 2 3 4 5 6

        #want loop to stop when the window touches the end of the main array i.e. last element. 
        # eg. when the window hits the end, window stops when it takes in acc first of the window and last of the window
        # i.e. -1 + 6. End.  

        total -= array[i]
        total += array[i+k]
        average = total / k
        averages.append(average) #at the end of the "processing", add to list of averages

    return averages

        

#return: list of averages
k = 5
array = [1,2,3,4,5,6,7,8,9,10]
print(slidingWindow_sizeKsubarray(k, array))
