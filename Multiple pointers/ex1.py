# ------------------------------ Question -----------------------------
# Write a function called sumZero which accepts a sorted array of integers.
# The function should find the first pair where the sum is 0.
#  Return an array that includes both values that sum to zero or undefined
#  if a pair does not exist
# ------------------------------ Solution -----------------------------
def sumZero(arr): 
    # take left = first index
    left = 0
    # take right = last index
    right = len(arr)-1
    # check if left < right, to avoid false positive
    while left<right:
        # if sum of left and right = 0
        print(left, right)
        if arr[left] + arr[right] == 0:
            # return array with left index value and right index value 
            return [{"indexes": [left, right], "values": [arr[left],arr[right] ]}]
            
        # if sum of left and right > 0
        elif arr[left] + arr[right] > 0:
            # decrease last index
            right -= 1
        # if sum of left and right < 0
        elif arr[left] + arr[right] < 0:
            # increase first index 
            left += 1
    return False

print(sumZero([-4,-3,-2,0,2,7])) # array must be ordered