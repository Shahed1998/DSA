# ------------------------------ Question -----------------------------
# Write a recursive function called reverse which accepts a string
# and returns a new string in reverse.
# ------------------------------ Solution -----------------------------

def reverse(st):

    if len(st) == 1: return st[0] # base case

    return st[-1] + reverse(st[:-1])

print(reverse("S"))