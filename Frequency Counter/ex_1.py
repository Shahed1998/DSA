# ---------------------------- Question ----------------------------
# Write a function called same, which accepts two arrays.
# The function should return true,
# if every value in the array has it's corresponding value squared in the second array.
# The frequency of values must be the same.
# ---------------------------- Solution ----------------------------
def same(arr1, arr2):
    # Checks if the arrays are of same length, if not same length return false else continue
    if len(arr1) != len(arr2):
        return False
    # declare one dictionary
    second = {}
    # use a for loop to store second array value in the dictionary as key
    for i in arr2: 
        if i in second.keys():
            # and increment the dictionary value if key available
            second[i] += 1
        else:
            # or place 1 as value 
            second[i] = 1 
    # print(second)
    # loop through first array
    for i in arr1:
        # exponent the values of indexes in first array 
            # check if key available in dictionary and also key value greater than 0 
            if i**2 in second.keys() and second[i**2]>0:
            # if available decrement count of values and loop again to next index
                second[i**2] = second[i**2]-1
                continue
            # if value less than 1 returns false
            return False
    # Return true when all key values are 0        
    # print(second)
    return True 

same([3,1,3], [1,9,9])
