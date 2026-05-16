class Solution:
    def mergeAlternately(self, word1, word2):
        word_arr = []
        min_wordLen = min(len(word1), len(word2))

        for i in range(min_wordLen):
            word_arr.append(word1[i])
            word_arr.append(word2[i])

        word_arr.append(word1[min_wordLen:])
        word_arr.append(word2[min_wordLen:])

        return ''.join(word_arr)


s = Solution()
print(s.mergeAlternately(word1 = "abc", word2 = "pqr"))
        
        