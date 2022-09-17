# ------------------------------ Question -----------------------------
# Write a function called sameFrequency.
# Given two positive integers, find out if the two numbers have the same frequency of digits.
# Your solution MUST have the following complexities: 0(N)
# ------------------------------ Solution -----------------------------
def sameFrequency (a,b):
    # check if both parameters are positive or return false
    if not (a>0 and b>0): return False
    # convert the parameters to string
    a,b = str(a), str(b)
    # check if both strings are of same length else return false
    if not len(a) == len(b): return False
    # take a dictionary 
    paramDict = {}
    # loop first parameter a and keep the index value as key 
    for i in a:
        # if index value already in dictionary increment value of the key
        if i in paramDict: paramDict[i] += 1
        # else put key value to 1
        else: paramDict[i] = 1
    # loop parameter b 
    for i in b:
        # check if not index of parameter b in dictionary
        # for corresponding index, key value > 0 return false
        if ((not i in paramDict) or (not paramDict[i] > 0)): return False 
        # else decrement value of the key
        paramDict[i] -= 1
    
    return True

print(sameFrequency(22,222))