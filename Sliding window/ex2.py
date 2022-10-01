# ------------------------------ Question -----------------------------
# Write a function called minSubArrayLen
# which accepts two parameters - an array of positive integers and a positive integer.
# This function should return the minimal length of a contiguous subarray
# of which the sum is greater than or equal to the integer passed to the function.
# If there isn't one, return 0 instead.
# ------------------------------ Solution -----------------------------

def minSubArrayLen(arr, num):

    if (not arr) or (not num) or (not int(num)) or (not num > 1):
        return 0

    for i in arr:
        if not int(i):
            return 0
        elif not i > 0:
            return 0

    window_left = window_right = 0
    min_sub_arr_len = float('inf')
    sum = 0

    while window_left < len(arr):
        if sum < num and window_right < len(arr):
            sum += arr[window_right]
            window_right += 1

        elif sum >= num:
            if min_sub_arr_len > (window_right - window_left):
                min_sub_arr_len = (window_right - window_left)

            sum -= arr[window_left]
            window_left += 1

        else: break
        

    return 0 if min_sub_arr_len == float('inf') else min_sub_arr_len

# ------------------------------ Test cases -----------------------------
print(minSubArrayLen([2,3,1,2,4,3], 7)) # 2 -> because [4,3] is the smallest subarray
print(minSubArrayLen([2,1,6,5,4], 9)) # 2 -> because [5,4] is the smallest subarray
print(minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52)) # 1 -> because [62] is greater than 52
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],39)) # 3
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],55)) # 5
print(minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11)) # 2
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],95)) # 0