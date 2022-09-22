# ------------------------------ Question -----------------------------
# Implement a function called, areThereDuplicates which accepts a variable number of arguments,
# and checks whether there are any duplicates among the arguments passed in.
# You can solve this using the frequency counter pattern OR the multiple pointers pattern.
# ------------------------------ Solution -----------------------------
# function that takes variable arguments
def areThereDuplicates(*args):
    # take a dictionary
    storage = {}
    # loop the arguments
    for arg in args:
        # if value not in dictionary store it as key
        if arg not in storage:
            storage[arg] = 1
        # if value already available return true
        else: return True
    # return false when no duplicates are found
    return False

print(areThereDuplicates('a', 'b', 'c'))