class Solution:
    def lengthOfLongestSubstring(self, s):
        
        hashMap = {}
        maxLen = 0
        left = 0

        for right in range(len(s)):

            while s[right] in hashMap:
                hashMap.pop(s[left])
                left += 1

            hashMap[s[right]] = 1
            maxLen = max(maxLen, right - left + 1)

        return maxLen





s = Solution()
print(s.lengthOfLongestSubstring("abba"))
# print(s.lengthOfLongestSubstring("dvdf"))
# print(s.lengthOfLongestSubstring(s = "au"))
# print(s.lengthOfLongestSubstring(s = ' '))
# print(s.lengthOfLongestSubstring(s = "bbbbb"))
# print(s.lengthOfLongestSubstring(s = "abcabcbb"))
# print(s.lengthOfLongestSubstring(s ="pwwkew"))