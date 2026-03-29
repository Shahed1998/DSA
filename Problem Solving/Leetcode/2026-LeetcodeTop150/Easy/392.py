class Solution:
    def isSubsequence(self, s, t):

        # Solve the follow-up after completing DP, Binary Search and how preprocessing works

        # The below code is applicable when frequency of s is small -> The time complexity is O(n), it can be further reduced to O(m)
        if len(si) <= 0: return True

        si = 0
        for i in t:
            if i != s[si]: continue
            si += 1

            if si == len(s): return True

        return False




s = Solution()
# print(s.isSubsequence(s = "abc", t = "bahbgdc"))
# print(s.isSubsequence(s = "aec", t = "abcde"))
# print(s.isSubsequence(s = "ace", t = "abcde"))
print(s.isSubsequence(s = "", t = "ahbgdc"))