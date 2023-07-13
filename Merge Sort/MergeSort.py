class MergeSort:

    # Public method
    def sort(self, arr):
        # Base case
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2  # Floor division
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.__merge(left, right)

    # Private method
    def __merge(self, arr1, arr2):
        i = 0  # pointer of arr1
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            elif arr1[i] == arr2[j]:
                result.append(arr1[i])
                result.append(arr2[j])
                i += 1
                j += 1
            else:
                result.append(arr2[j])
                j += 1

        # once one array is exhausted, remaining values of the other array
        # is pushed into the result

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result


ms = MergeSort()
print(ms.sort([73, 10, 76, 24]))
