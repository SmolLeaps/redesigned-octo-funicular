"""
Find the length of the substring with no longer than K distinct characters.
Difficulty: Medium

Task requirements
- identify the 
store the longest substrings(s) which satisfy the condition - 

if you want debugging logs at each iteration of the for loop, uncomment lines 21 to 31.
"""

def longestSubstring(inputString, k):
    windowStart = 0
    windowString = ''
    longestSubstringLength = 0
    #keep iterating through the string...
    for windowEnd in range(0, len(inputString)):
        windowString += inputString[windowEnd]
        print("window start:", windowStart, "window end:", windowEnd)
        print("current window sum: ", windowString)
        
        numDistinctCharacters = len(set(windowString))
        print("numDistinctCharacters", numDistinctCharacters, "\n")

        #until there are more than K distinct characters
        while numDistinctCharacters > k:
            print("NUM DISTINCT CHARS EXCEEDED GIVEN CONSTRAINT k...")
            print("current window sum: ", windowString)
            windowStart += 1
            windowString = inputString[windowStart:windowEnd+1]
            numDistinctCharacters = len(set(windowString))

            print("new windowString:", windowString, "\n")
        if len(windowString) > longestSubstringLength:
            longestSubstringLength = len(windowString)
    return longestSubstringLength 

print(
    "results:",
    longestSubstring("araaci", 2), # should be 4 ("araa")
    longestSubstring("araaci", 1), # should be 2 ("aa")
    longestSubstring("aaaarrr", 1), #should be 4 ("aaaa"): previous larger lengths should not be overwritten by
    longestSubstring("aaarrrr", 1), #should be 4
    longestSubstring("aaarrrraaaaa", 1), #should be 4
)