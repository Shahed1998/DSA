# ------------------------------ Question -----------------------------
# Write a function called isSubsequence
# which takes in two strings and checks 
# whether the characters in the first string form a subsequence of 
# the characters in the second string. 
# In other words, the function should check whether the characters in the first string
# appear somewhere in the second string, without their order changing.
# ------------------------------ Solution -----------------------------
def isSubsequence(str1, str2):
    # check if both parameters are available
    if (not str1) or (not str2):
        return False
    # convert both parameters to string
    str1 = str(str1)
    str2 = str(str2)
    # take two pointers 
    p1 = 0 # points to str1
    p2 = 0 # points to str2

    while p2 < len(str2):

        if str1[p1] == str2[p2]:
            p1 += 1
        
        if p1 == len(str1):
            return True

        p2 +=1

    return False


print(isSubsequence('abc', 'acb'))