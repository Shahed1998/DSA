class Solution:
    def strStr(self, haystack, needle):
        
        if needle == "": return 0



        for i in range(len(haystack)-len(needle)+1):
            count = 0
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]: break
                else: count += 1

            if count == len(needle): return i
        
        return -1
             



s = Solution()
# print(s.strStr(haystack="abc", needle="bc"))
# print(s.strStr(haystack = "sadbutsad", needle = "sad"))
# print(s.strStr(haystack = "leetcode", needle = "lieto"))
# print(s.strStr(haystack= "hello", needle= "ll"))

