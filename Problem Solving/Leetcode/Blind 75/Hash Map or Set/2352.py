class Solution:
    def equalPairs(self, grid):

        rows = {}
        combinations = 0

        for i in range(len(grid)):

            st = ','.join(map(str, grid[i]))

            if st in rows:
                rows[st] += 1
            else:
                rows[st] = 1
                

        for i in range(len(grid)):

            tmp = []

            for j in range(len(grid)):

                tmp.append(grid[j][i])

            c = ','.join(map(str, tmp))
            
            if c in rows:
                combinations += rows[c] 

        print(combinations)
        return combinations




s = Solution()
s.equalPairs(grid = [[11,1],[1,11]])
s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
s.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])
s.equalPairs(grid = [[13,13],[13,13]])