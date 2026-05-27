class Solution:
    def closeStrings(self, word1, word2):

        if len(word1) != len(word2): return False

        w1 = {}
        w2 = {}

        for w in word1:
            w1[w] = 1 if w not in w1 else w1[w] + 1
            

        for w in word2:
            w2[w] = 1 if w not in w2 else w2[w] + 1

        # True if counter w1 and w2 have same set of keys and same set of keys after sorting else False
        return (set(w1.keys()) == set(w2.keys()) 
                and sorted(w1.values()) == sorted(w2.values()))




s = Solution()
print(s.closeStrings(word1 = "cabbbad", word2 = "dabbccc"))
print(s.closeStrings(word1 = "a", word2 = "aa"))
print(s.closeStrings(word1 = "abc", word2 = "bca"))