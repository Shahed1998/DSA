class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    # Insertion using the bubble up technique
    def insert(self, element):
        self.values.append(element)
        self.bubbleUp()

    def bubbleUp(self):
        idx = len(self.values) - 1
        while True:
            pIdx = (idx-1)//2
            if pIdx < 0 or self.values[idx] < self.values[pIdx]:
                return
            temp = self.values[pIdx]
            # Swapping values
            self.values[pIdx] = self.values[idx]
            self.values[idx] = temp
            idx = pIdx

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
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            leftChildVal = 0
            rightChildVal = 0
            parentVal = self.values[idx]
            swap = None
            # If right child index is in the range of the array
            # That means left child index is also in the range
            if rightChildIdx < len(self.values):
                leftChildVal = self.values[leftChildIdx]
                rightChildVal = self.values[rightChildIdx]
                if leftChildVal < rightChildVal:
                    swap = rightChildIdx
                elif leftChildVal > rightChildVal:
                    swap = leftChildIdx
            # If the parent has only left child but not right
            elif leftChildIdx < len(self.values):
                leftChildVal = self.values[leftChildIdx]
                if parentVal < leftChildVal:
                    swap = leftChildIdx
            if swap == None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = parentVal
            idx = swap
            swap = None


# ------------------------------------------------------------
# Test cases
# ------------------------------------------------------------
mbh = MaxBinaryHeap()
mbh.insert(10)
mbh.insert(30)
mbh.insert(20)
mbh.insert(40)
mbh.insert(50)
mbh.insert(70)
mbh.insert(60)
print("After insertion:", mbh.values)
print(mbh.extractMax())
print("After extracting max:", mbh.values)
