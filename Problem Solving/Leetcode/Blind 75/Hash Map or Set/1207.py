class Solution:
    def uniqueOccurrences(self, arr):

        hashmap = {}
        value = set()

        for el in arr:

            if el not in hashmap:
                hashmap[el] = 1
            else:
                hashmap[el] += 1

        for key in hashmap:
            
            value_of_key = hashmap[key]

            if value_of_key in value:
                return False

            value.add(value_of_key)


        return True


        

s = Solution()
print(s.uniqueOccurrences(arr = [1,2,2,1,1,3]))
print(s.uniqueOccurrences(arr = [1,2]))
print(s.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))