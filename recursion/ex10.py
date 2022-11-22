# ------------------------------ Question -----------------------------
# Write a recursive function called capitalizeFirst.
# Given an array of strings, capitalize the first letter of each string in the array.
# ------------------------------ Solution -----------------------------
def capitalizeFirst(arr):

    # return [x[0].upper()+ x[1:].lower() for x in arr] #Iterative

    # Recursive
    if len(arr) == 0: return []

    x = arr.pop(0)

    return [x[0].upper()+x[1:].lower()] + capitalizeFirst(arr)

print(capitalizeFirst(['car','taco','banana']))