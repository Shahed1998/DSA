class Solution:
    def reverseWords(self, s: str):

        end = None
        result = []

        for i in range(len(s)-1, -1, -1):
            
            if s[i] == ' ':
                if end != None:
                    result.append(s[i+1:end+1])
                end = None

            elif end == None:
                end = i

        if end != None:
            result.append(s[0:end+1])

        return ' '.join(result)


        # Automated split
        # s_arr = s.split() # shortcut

        # lptr = 0
        # rptr = len(s_arr)-1


        # while lptr < rptr:

        #     tmp = s_arr[lptr]

        #     s_arr[lptr], s_arr[rptr] = s_arr[rptr], s_arr[lptr]

        #     lptr += 1
        #     rptr -= 1


        # return ' '.join(s_arr)


s = Solution()
print(s.reverseWords(s = "the sky is blue"))
print(s.reverseWords(s = "  hello world  "))
print(s.reverseWords(s = "a good   example"))