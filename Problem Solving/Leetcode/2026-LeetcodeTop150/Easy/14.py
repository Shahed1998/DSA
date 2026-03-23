class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        lP = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < len(lP) and j < len(strs[i]) and lP[j] == strs[i][j]:
                j += 1

            lP = lP[:j]

            if lP == "":
                return ""

        return lP

s = Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(s.longestCommonPrefix(strs = ["dog","racecar","car"]))
print(s.longestCommonPrefix(["cir","car"]))
print(s.longestCommonPrefix(["aaa","aa","aaa"]))