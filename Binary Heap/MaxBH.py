class MaxBinaryHeap:
    def __init__(self):
        self.values = []
    
    # Insertion using the bubble up technique
    def insert(self, element):
        self.values.append(element)
        self.bubbleUp()

    def bubbleUp(self):
        cIdx = len(self.values) - 1
        while(cIdx > 0):
            pIdx = (cIdx-1)//2
            if self.values[cIdx] < self.values[pIdx]: break
            temp = self.values[pIdx]
            self.values[pIdx] = self.values[cIdx]
            self.values[cIdx] = temp
            cIdx = pIdx
    
    def extractMax(self):
        ret = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.bubbleDown()
        return ret
    
    def bubbleDown(self):
        idx = 0
        while True:
            leftChildIdx  = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            leftChildVal = 0; rightChildVal = 0
            parentVal = self.values[idx]
            swap = None
            if leftChildIdx < len(self.values):
                leftChildVal  = self.values[leftChildIdx]
                if parentVal < leftChildVal: swap = leftChildIdx
            if rightChildIdx < len(self.values):
                rightChildVal = self.values[rightChildIdx]
                if leftChildVal < rightChildVal: swap = rightChildIdx
                elif leftChildVal > rightChildVal: swap = leftChildIdx
            if swap == None: break
            self.values[idx] = self.values[swap]
            self.values[swap] = parentVal
            idx = swap
            swap = None


mbh = MaxBinaryHeap()
mbh.insert(55)
mbh.insert(39)
mbh.insert(41)
mbh.insert(18)
mbh.insert(27)
mbh.insert(12)
print("After insertion:", mbh.values)
print(mbh.extractMax())
print("After extracting max:", mbh.values)

