class Solution:
    def removeStars(self, s):

        # ---------------------------------------------------------
        # Stack approach
        # ---------------------------------------------------------
        stack = []

        for el in s:

            if el == "*":
                stack.pop()
            else:
                stack.append(el)

        return ''.join(stack)


        # ---------------------------------------------------------
        # My proposed solution 
        # ---------------------------------------------------------

        # star_removed = 0
        # result = []

        # for i in range(len(s)-1, -1, -1):

        #     if star_removed >= 1 and s[i] != '*':
        #         star_removed -= 1 
        #         continue

        #     if s[i] == '*':
        #         star_removed += 1
        #         continue

        #     result.append(s[i])

        # return ''.join(result[::-1])



s = Solution()
s.removeStars(s = "leet**cod*e")
s.removeStars(s = "erase*****")
        