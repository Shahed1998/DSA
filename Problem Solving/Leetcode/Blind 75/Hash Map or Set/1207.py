class Solution:
    def uniqueOccurrences(self, arr):

        counter = dict()
        occurrences = set()

        for n in arr:
            counter[n] = counter.get(n, 0) + 1

        for n in counter.values():
            
            if n in occurrences:
                return False

            occurrences.add(n)

        return True



        

s = Solution()
print(s.uniqueOccurrences(arr = [1,2,2,1,1,3]))
print(s.uniqueOccurrences(arr = [1,2]))
print(s.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))