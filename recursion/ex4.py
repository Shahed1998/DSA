# ------------------------------ Question -----------------------------
# Write a function called recursiveRange
# which accepts a number and adds up all the numbers
# from 0 to the number passed to the function 
# ------------------------------ Solution -----------------------------
def recursiveRange(num):

    if num < 1: return 0 # base case

    return num + recursiveRange( num-1 )

print(recursiveRange(997))
