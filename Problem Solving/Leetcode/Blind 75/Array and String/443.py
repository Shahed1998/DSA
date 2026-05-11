class Solution:
    def compress(self, chars):

        i = 0
        res = 0

        while i < len(chars):
            group_length = 1

            while i + group_length < len(chars) and chars[i+group_length] == chars[i]:
                group_length += 1 

            chars[res] = chars[i]
            res += 1

            if group_length > 1:
                str_rpr = str(group_length)
                chars[res:res+len(str_rpr)] = list(str_rpr)
                res += len(str_rpr)

            i += group_length

        return res

             



s = Solution()
# s.compress(["a","a","b","b","c","c","c"])
# s.compress(["a"])
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))