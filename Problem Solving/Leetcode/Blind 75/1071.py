from math import gcd 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # 1. Check if they share the same 'vibe' (periodic pattern).
        # If str1 + str2 == str2 + str1, they MUST be made of the same repeating unit.
        if str1 + str2 != str2 + str1:
            return ""

        # 2. If they share a pattern, the longest repeating unit's length 
        # is the Greatest Common Divisor (GCD) of the two string lengths.
        return str2[:gcd(len(str1), len(str2))]



s = Solution()
print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "AAAAAB", str2 = "AAA"))
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))

