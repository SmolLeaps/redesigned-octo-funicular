"""
Find the length of the substring with no longer than K distinct characters.
Difficulty: Medium

Task requirements
- identify the 
store the longest substrings(s) which satisfy the condition - 

if you want debugging logs at each iteration of the for loop, uncomment lines 21 to 31.
"""

def longestSubstring(inputString, k):
    finalSubstring = '1'
    windowStart = 0
    memo = ''
    windowSum = ''
    largestWindowSums = [inputString[0]]
    #keep iterating through the string...
    for windowEnd in range(0, len(inputString)):
        windowSum += inputString[windowEnd]
        #print("current window sum: ", windowSum)
        
        numDistinctCharacters = len(set(windowSum))
        #print("numDistinctCharacters", numDistinctCharacters, "\n")
        #until there are more than K distinct characters
        if numDistinctCharacters > k:
            #print("NUM DISTINCT CHARS EXCEEDED GIVEN CONSTRAINT k...")
            # print("current window sum: ", windowSum)
            windowStart += 1
            windowSum = inputString[windowStart:windowEnd]
            #print("new windowSum:", windowSum, "\n")
        elif windowSum not in largestWindowSums and len(windowSum) >= len(max(largestWindowSums, key=len)):
            largestWindowSums.append(windowSum)
        else: 
            continue
        #print(max(largestWindowSums, key=len))
        #stop when the substring is back to 2 distinct characters
        #print('current window sum at the end of loop:', windowSum, ' distinct chars: ', numDistinctCharacters) 

    return max(largestWindowSums, key=len)

print(
    "results:",
    longestSubstring("araaci", 2), # should be 4 ("araa")
    longestSubstring("araaci", 1), # should be 2 ("aa")
    longestSubstring("aaaarrr", 1), #should be 4 ("aaaa"): previous larger lengths should not be overwritten by
    longestSubstring("aaarrrr", 1), #should be "rrrr",4
    longestSubstring("aaarrrraaaa", 1), #should be "rrrr" and "aaaa",4
)