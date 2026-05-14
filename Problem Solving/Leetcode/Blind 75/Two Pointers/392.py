class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tptr = 0
        lenOf_sMatched = 0

        for sptr in s:

            while tptr < len(t):

                if sptr == t[tptr]:
                    lenOf_sMatched += 1
                    tptr += 1
                    break

                tptr += 1

            if lenOf_sMatched == len(s): return True # early exit

        return lenOf_sMatched == len(s)

        

s = Solution()
# s.isSubsequence(s = "abc", t = "ahbgdc")
# s.isSubsequence(s = "axc", t = "ahbgdc")
print(s.isSubsequence(s ="aaaaaa", t = "bbaaaa"))