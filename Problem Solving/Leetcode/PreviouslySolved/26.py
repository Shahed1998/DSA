def removeDuplicates(nums):
    i = 0

    for j in range(len(nums)):
        if i == 0 or nums[i-1] != nums[j]:
            nums[i] = nums[j]
            i += 1

    return i



print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

