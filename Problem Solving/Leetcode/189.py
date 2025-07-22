def rotate(k, nums):

        arrLen = len(nums)

        if arrLen > 1 and k > 0:

            isEven = arrLen % 2 == 0

            if isEven or arrLen < 5:
                l = arrLen-k
                m = l
            else:
                l = arrLen-1-k
                m = l+1

            v = nums[l]

            nums[l] = nums[0]

            if isEven: nums[0] = v
            else: nums[0] = nums[m]

            for i in range(1, l):
                p = nums[i]
                nums[i] = nums[m+i]

                if(isEven): nums[m+i] = p
                else: nums[m+i-1] = p
            
            if not isEven: nums[arrLen-1] = v

        return nums          


# print(rotate(3, [1,2,3,4,5,6,7]))
# print(rotate(2, [-1,-100,3,99])) 
print(rotate(0, [1])) 
print(rotate(2, [1,2,3])) 
