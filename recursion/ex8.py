# ------------------------------ Question -----------------------------
# Write a recursive function called someRecursive
# which accepts an array and a callback.
# The function returns true if a single value in the array returns true
# when passed to the callback. Otherwise it returns false.
# ------------------------------ Solution -----------------------------

def isOdd(val): return (val % 2 != 0);

def isGreater(val): return val > 10

def someRecursive(array, callback):

    if len(array) == 0: return False

    elif callback(array[0]): return callback(array[0])

    return someRecursive(array[1:], callback)

print(someRecursive([4,6,8], isGreater))    


