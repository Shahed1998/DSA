# ------------------------------ Question -----------------------------
# Write a recursive function called isPalindrome
# which returns true if the string passed to it is a palindrome
# (reads the same forward and backward). Otherwise it returns false.
# ------------------------------ Solution -----------------------------

def isPalindrome(st):

    if len(st) == 1: return True

    elif st[0] != st[-1]: return False

    return isPalindrome(st[1:-1])


print(isPalindrome("awesome"))