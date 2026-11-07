class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "": return True

        slow = 0
    
        for ch in t:
            if ch == s[slow]:
                slow += 1

            if slow == len(s):
                return True

        return False



s = Solution()
# s.isSubsequence(s = "abc", t = "ahbgdc")
# s.isSubsequence(s = "axc", t = "ahbgdc")
print(s.isSubsequence(s ="aaaaaa", t = "bbaaaa"))