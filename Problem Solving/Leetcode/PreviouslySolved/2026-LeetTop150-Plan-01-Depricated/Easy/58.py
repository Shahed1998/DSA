class Solution:
    def lengthOfLastWord(self, s):
        wl = 0
        i = len(s)-1

        while i >= 0:
            
            if wl > 0 and s[i] == " ": break

            if s[i] != " ": wl += 1

            i -= 1
  
        return wl


s = Solution()
# s.lengthOfLastWord(s = "World        ")
# s.lengthOfLastWord(s = "Hello World")
# s.lengthOfLastWord(s = "   fly me   to   the moon  ")
# s.lengthOfLastWord(s = "luffy is still joyboy")
