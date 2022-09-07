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
    # use a for loop to store
    for i in arr2:
        # second array value in the dictionary as key 
        if i in second.keys():
            # and increment the dictionary value if key available
            second[i] += 1
        else:
            # or place 1 as value 
            second[i] = 1 
         
    print(second)
    # loop through first array
        # exponent the values of indexes in first array 
            # check if value available in dictionary 
            # if available decrement count of values
            # if value less than 1 returns false
    # return true 

same([1,2,3], [1,4,9])
