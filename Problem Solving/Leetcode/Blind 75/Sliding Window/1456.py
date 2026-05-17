class Solution:
    def maxVowels(self, s, k):

        max_vowels = 0

        vowels = set('AEIOUaeiou')

        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1

        tmp_vowels = max_vowels

        for right in range(k, len(s), 1):

            tmp_vowels += (1 if s[right] in vowels else 0) - (1 if s[right-k] in vowels else 0)

            max_vowels = max(max_vowels, tmp_vowels)

        return max_vowels



        



s = Solution()
print(s.maxVowels(s = "leetcode", k = 3))
print(s.maxVowels(s = "abciiidef", k = 3))