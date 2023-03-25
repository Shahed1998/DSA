class MaxBinaryHeap:
    def __init__(self):
        self.values = []
    
    # Insertion using the bubble up technique
    def insert(self, element):
        self.values.append(element)
        cIdx = len(self.values) - 1
        while(cIdx > 0):
            pIdx = (cIdx-1)//2
            if self.values[cIdx] < self.values[pIdx]: break
            temp = self.values[pIdx]
            self.values[pIdx] = self.values[cIdx]
            self.values[cIdx] = temp
            cIdx = pIdx
        

mbh = MaxBinaryHeap()
mbh.insert(41)
mbh.insert(39)
mbh.insert(33)
mbh.insert(18)
mbh.insert(27)
mbh.insert(12)
mbh.insert(55)
print(mbh.values)

