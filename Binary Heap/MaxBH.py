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
        swap = self.values.pop()
        ret = self.values[0]
        self.values[0] = swap
        print(self.values)
        self.bubbleDown()
        print(self.values)
        return ret
    
    def bubbleDown(self):
        swap = 0
        while(swap < len(self.values)/2-1):
            lci = 2*swap+1 # lci = left child index
            rci = 2*swap+2 # rci = right child index
            swapVal = self.values[swap]
            leftVal = self.values[lci]
            rightVal = self.values[rci]
            if swapVal < leftVal and swapVal < rightVal:
                if leftVal < rightVal:
                    self.values[swap] = rightVal
                    self.values[rci] = swapVal
                    swap = rci
                elif leftVal > rightVal:
                    self.values[swap] = leftVal
                    self.values[lci] = swapVal
                    swap = lci
            elif swapVal < leftVal:
                self.values[swap] = leftVal
                self.values[lci] = swapVal
                swap = lci
            elif swapVal < rightVal:
                self.values[swap] = rightVal
                self.values[rci] = swapVal
                swap = rci

mbh = MaxBinaryHeap()
mbh.insert(55)
mbh.insert(39)
mbh.insert(33)
mbh.insert(18)
mbh.insert(27)
mbh.insert(12)
# mbh.insert(55)
print(mbh.extractMax())

