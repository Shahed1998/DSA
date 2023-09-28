class SelectionSort:
    # Sorts only number
    def sort(self, arr):
        if len(arr) < 2:
            return arr
        left_ptr = 0
        right_ptr = left_ptr + 1
        while left_ptr < len(arr):
            while right_ptr < len(arr):
                print(left_ptr, right_ptr)
                temp = arr[left_ptr]
                if arr[right_ptr] < arr[left_ptr]:
                    arr[left_ptr] = arr[right_ptr]
                    arr[right_ptr] = temp
                right_ptr += 1
            left_ptr += 1
            right_ptr = left_ptr + 1
        return arr


ss = SelectionSort()
print(ss.sort([10, 1, 3, 2, 11, 5, 3, 20, 9, 4]))
print(ss.sort(["B", "A", "D", "C", "F", "E"]))
