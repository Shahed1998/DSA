# ---------------------------- Question ----------------------------
# Given two strings,
# write a function to determine if the second string is an anagram of the first. 
# An anagram is a word, phrase, or name formed by rearranging the letters of another, 
# such as cinema, formed from iceman.

def isAnagram(str1,str2):
    # check if both input are strings and both are of same lengths
    # if not then return false
    if not (isinstance(str1,str) and isinstance(str2,str) and len(str1) == len(str2)):
        return False

    # take an empty dictionary to store characters of string 1
    storage = {}

    # loop 1: string 1 and store characters as key and values as the character count
    for i in str1:
        if i in storage:
            storage[i] += 1
        else:
             storage[i] = 1

    # loop 2: use it to loop through the second string 
        # if the character not present in the string return False
        # if the value less than or equals to 0, return False
    for i in str2:
        if (not i in storage) or (storage[i]<=0):
            return False 
        else:
            storage[i] -= 1

    #return True
    return True



print(isAnagram("ewe", "wee"))