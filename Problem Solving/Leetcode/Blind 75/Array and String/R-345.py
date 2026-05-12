class Solution:
    def reverseVowels(self, s):

        vowels = set("AEIOUaeiou")
        lptr = 0
        rptr = len(s)-1
        s_list = list(s)
        

        while lptr < rptr:

            if s_list[lptr] not in vowels:
                lptr += 1
            
            elif s_list[rptr] not in vowels:
                rptr -= 1
            
            else:
                s_list[lptr], s_list[rptr] = s_list[rptr], s_list[lptr]
                lptr += 1
                rptr -= 1

        
        return "".join(s_list)


                



s = Solution()
print(s.reverseVowels(s = "IceCream"))
print(s.reverseVowels(s = "leetcode"))