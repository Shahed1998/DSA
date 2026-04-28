class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # step 01: we have to compare whether str1 + str2 = str2 + str1
        ## if they are equal then we can say str2 is GCD of str1, return it
        # step 02: if not we will recurse and reduce str2 elements from the right and again compare until there is no elements left in str2

        if len(str2) <= 0 or (str1 + str2 == str2 + str1 and len(str1) % len(str2) == 0) : return str2

        return self.gcdOfStrings(str1, str2[:-1])
        


s = Solution()
print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "AAAAAB", str2 = "AAA"))
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))

