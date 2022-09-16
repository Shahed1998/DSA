# ------------------------------ Question -----------------------------
# Implement a function called countUniqueValues,
# which accepts a sorted array, and counts the unique values in the array.
# There can be negative numbers in the array, but it will always be sorted.
# ------------------------------ Solution -----------------------------
def countUniqueValues(arr):
    # check if the length of the array less than 2, if true return 0
    if len(arr) < 2:
        return 0

    # take two pointers
    left = 0
    right = 1

    # Time and space complexity 0(n) 
    # checks if left less than right and right less than the length of the array
    # if left index value not equal to right then increase left index and change it's value 
    # to right index value and increment the right index
    while ((left < right) and (right <= len(arr)-1)):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]
            
        right += 1
    
    return left+1


print(countUniqueValues([-2,-1,-1,0,1]))