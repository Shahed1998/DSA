class Solution:
    def increasingTriplet(self, nums):
        result = False

        i = 0
        iVal = nums[0]
        iIndex = 0

        while i < len(nums)-2:
            
            if iVal > nums[i]:
                iVal = nums[i]
                iIndex = i

            i += 1

        j = iIndex
        jVal = -1
        jIndex = -1

        while j < len(nums)-1:
            if iVal < nums[j]:
                jVal = nums[j]
                jIndex = j

            j += 1


        k = jIndex
        kVal = -1
        kIndex = -1

        while k < len(nums):
            if kVal < nums[k]:
                kVal = nums[k]
                kIndex = k

            k += 1
        

        return (iIndex < jIndex < kIndex) and (iVal < jVal < kVal)
            

s = Solution()
s.increasingTriplet([2,1,5,0,4,6])