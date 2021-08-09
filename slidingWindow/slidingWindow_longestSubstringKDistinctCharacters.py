"""
Find the length of the substring with no longer than K distinct characters.
Difficulty: Medium
"""

def longestSubstring(inputString, k):
    finalSubstring = '1'
    windowStart = 0
    memo = ''
    windowSum = ''

    #keep iterating through the string...
    for windowEnd in range(0, len(inputString)):
 
        windowSum += inputString[windowEnd]
        numDistinctCharacters = len(set(inputString[windowStart:windowEnd]))
        #until there are more than K distinct characters
        if numDistinctCharacters > k: 
            windowSum = windowSum[1:]
            #print("NUM DISTINCT CHARS EXCEEDED GIVEN CONSTRAINT k. new windowSum:", windowSum)
        #stop when the substring is back to 2 distinct characters
        #print('current window sum at the end of loop:', windowSum, ' distinct chars: ', numDistinctCharacters) 

    return windowSum

print(
    "results:",
    longestSubstring("araaci", 2), # should be 4 ("araa")
    longestSubstring("araaci", 1) # should be 2 ("aa")
)