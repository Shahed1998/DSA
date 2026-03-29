class Solution:
    def isPalindrome(self, s):

        # Not necessary, every pl have built in function
        alNum = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0,
                'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, '0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0 }
        

        left = 0; right = len(s)-1

        while left < right: 

            if s[left].lower() not in alNum:
                left += 1
                continue

            if s[right].lower() not in alNum:
                right -= 1
                continue

            if s[right].lower() != s[left].lower(): 
                return False

            left += 1
            right -= 1

        return True





        # Time complexity O(n) and Space Complexity O(N)
        # forward = ''
        # backward = ''
        

        # for i in s:
        #     if i.lower() in dict:
        #         forward += i.lower()



        # for i in s[::-1]:
        #     if i.lower() in dict:
        #         backward += i.lower()


        # print(forward)
        # return forward == backward




s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
# print(s.isPalindrome(""))
# print(s.isPalindrome("0P"))


'amanaplanacanalpanama'