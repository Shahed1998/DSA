# ------------------------------ Question -----------------------------
# Given an array of integers and a number, write a function called maxSubarraySum,
# which finds the maximum sum of a subarray with the length of the number passed to the function.
# Note that a subarray must consist of consecutive elements from the original array.
# In the first example below, [100, 200, 300] is a subarray of the original array,
# but [100, 300] is not.
# ------------------------------ Solution -----------------------------
def maxSubarraySum(arr, elem):
    if (not arr) or (not elem) or (len(arr)<elem):
        return False
    temp = 0
    for i in range(elem):
        temp += arr[i]
    max = temp
    for i in range(elem, len(arr)):
        temp = temp + arr[i] - arr[i-elem]
        if max < temp: max = temp
    return max
    
# ------------------------------ Test cases -----------------------------
# maxSubarraySum([100,200,300,400], 2) #700
# maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)  #39 
# maxSubarraySum([-3,4,0,-2,6,-1], 2) #5
# maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) #5
print(maxSubarraySum([2,3], 3)) # null
