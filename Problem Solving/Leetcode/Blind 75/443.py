class Solution:
    def compress(self, chars):

        lptr = 0
        group_length = 0

        for rptr in range(len(chars)):
            
            if chars[rptr] == chars[lptr]:
                group_length += 1
                continue

            if group_length == 0:
                lptr += 1
                continue
            
            lptr += 1
            chars[lptr] = group_length
            lptr += 1
            chars[lptr] = chars[rptr]
            group_length = 1

        print(lptr, group_length)
        if group_length > 1:
            chars[lptr+1] = group_length


        print(chars)
             



s = Solution()
# s.compress(["a","a","b","b","c","c","c"])
# s.compress(["a"])
s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])