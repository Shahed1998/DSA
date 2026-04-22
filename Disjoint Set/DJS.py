class Solution:
    def __init__(self, n):
        self.djs = [i for i in range(n)]

    # Without path compression
    # def find(self, x):
    #     if self.djs[x] != x: 
    #         return self.find(self.djs[x])
    #     return x
    
    # With path compression / flattening
    def find(self, x):
        if self.djs[x] != x:
            self.djs[x] = self.find(self.djs[x])  # flatten
        return self.djs[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if(rootX != rootY):
            self.djs[rootY] = rootX
        else:
            print("Cycle detected")

    def Print(self):
        print(self.djs)

            

s = Solution(4)

s.union(0,1)
s.union(1,2)
s.union(2,3)
s.union(3,0)


