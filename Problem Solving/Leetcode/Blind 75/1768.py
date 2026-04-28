class Solution:
    def mergeAlternately(self, word1, word2):

        result = []
        minLen = min(len(word1), len(word2))

        
        for i in range(minLen):

            result.append(word1[i])
            result.append(word2[i])

        result.append(word1[minLen:])
        result.append(word2[minLen:])

        return ''.join(result)



s = Solution()
s.mergeAlternately(word1 = "abcd", word2 = "pq")