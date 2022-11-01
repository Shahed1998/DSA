# ------------------------------ Question -----------------------------
# Write a function called productOfArray
# which takes in an array of numbers and returns the product of them all.
# ------------------------------ Solution -----------------------------

def productOfArray(nums):

    if len(nums) < 1: return 1 # base case
    return nums.pop() * productOfArray(nums)



print(productOfArray([1,2,3])) # 6
print(productOfArray([1,2,3,10])) # 60