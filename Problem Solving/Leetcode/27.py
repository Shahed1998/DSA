def removeElement(nums, val):
    numsLen = len(nums)-1
    i = j = numsLen
    while i >= 0:
        if(nums[i] == val and nums[j] == val): j -= 1
        elif(nums[i] == val and nums[j] != val):
            nums[i]=nums[j]
            nums[j]=val
            j -= 1

        i -= 1
    return j+1

print(removeElement([0,1,2,2,3,0,4,2], 2)) # Output: 5, nums = [0,1,4,0,3,_,_,_]
