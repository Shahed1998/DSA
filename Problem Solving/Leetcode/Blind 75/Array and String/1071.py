from math import gcd 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def fnGCD(a,b):
            while b != 0:
                a, b = b, a % b
            
            return a

        return str2[:fnGCD(len(str1), len(str2))]



s = Solution()
print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "AAAAAB", str2 = "AAA"))
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))

