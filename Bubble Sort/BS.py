# Bubble sort
class BS:
    @staticmethod
    def sort(array):
        # print("i", "j", "j+1", "array")
        for i in reversed(range(len(array))):
            # ----------------------------------------
            # comparisons
            # ----------------------------------------
            # j starts from 0 until i-1
            # j+1 == i
            # swaps checks after a complete iteration of j is done
            # for a new iteration of i, swap value changes to false
            # if a value is swapped, it is changed to true
            # and hence swap doesn't break out of the loop, or else it breaks
            swaps = False
            for j in range(i):
                if (array[j] > array[j+1]):
                    # swapping
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swaps = True
                # print(i, j, j+1, array)
            if not swaps:
                break
        return array


bs = BS.sort([2, 5, 2, 1, 3, 14, 10])
print(bs)
