# Find the count of all the alphaNumeric characters in an input string
# take user input
inp = input("Enter string: ")
# convert to lower case
inp = inp.lower()
# create a dictionary
char = {}
# loop through the string
for ch in inp: 
    # check if the character is alphaNumeric by using ascii value
    if (ord(ch)>47 and ord(ch)<58) or (ord(ch)>96 and ord(ch)<123):
        # check if the character in dictionary
        if ch in char:
            char[ch] = char[ch]+1
        else:
            # if not in dictionary input character = 1 else increment it
            char[ch] = 1
        
print(char)
