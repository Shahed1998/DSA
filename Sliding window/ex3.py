# ------------------------------ Question -----------------------------
# Write a function called findLongestSubstring,
# which accepts a string and returns the length of the longest substring
# with all distinct characters
# ------------------------------ Solution -----------------------------

def findLongestSubstring(s): 
        
    charSet = set()
    left = 0
    res = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1 
        
        charSet.add(s[right])
        res = max(res, right-left+1)

    return res


    
    

# ------------------------------ Test cases -----------------------------
print(findLongestSubstring("pwwkew")) # 0
# print(findLongestSubstring('rithmschool')) # 7
# print(findLongestSubstring('thisisawesome')) # 6
# print(findLongestSubstring('thecatinthehat')) # 7
# print(findLongestSubstring('bbbbbb')) # 1
# print(findLongestSubstring('longestsubstring')) # 8
# print(findLongestSubstring('thisishowwedoit')) # 6