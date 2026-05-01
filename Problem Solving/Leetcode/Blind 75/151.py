class Solution:
    def reverseWords(self, s: str):

        # Manual Split
        s_arr = []
        tracker = None

        for i in range(len(s)-1, -1, -1):

            if s[i] != ' ' and tracker == None:
                tracker = i

            if s[i] == ' ' and tracker != None:
                s_arr.append(s[i+1: tracker+1])
                tracker = None

            if i == 0 and tracker != None:
                s_arr.append(s[i: tracker+1])
                tracker = None


        return ' '.join(s_arr)


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