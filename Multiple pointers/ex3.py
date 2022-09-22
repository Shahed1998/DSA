# ------------------------------ Question -----------------------------
# Write a function called averagePair. 
# Given a sorted array of integers and a target average,
# determine if there is a pair of values in the array where the average of the pair equals
# the target average. There may be more than one pair that matches the average target.
# ------------------------------ Solution -----------------------------
def averagePair(arr, avg):
    # if arr empty return false
    if len(arr) <= 1:
        return False 
    # multiply the by 2
    avg *=2
    # take two pointers pointing first and last index
    first = 0
    last = len(arr)-1
    
    # if sum of first and last index value
    while first < last:
        # if sum of first and last index value
        # equals to average then return true
        if arr[first] + arr[last] == avg:
            return True
        # greater than average, decrement the last index
        if arr[first] + arr[last] > avg:
            last -= 1
            continue
        # if sum of first and last index value
        # less than average, increment the first index
        if arr[first] + arr[last] < avg:
            first += 1
    # if none available return false
    return False

print(averagePair([],4))