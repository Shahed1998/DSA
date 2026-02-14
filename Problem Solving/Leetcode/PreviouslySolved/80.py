def removeDuplicates(nums):
    i = 0

    for j in range(len(nums)):
        if i == 0 or i == 1 or nums[i-2] != nums[j]:
            nums[i] = nums[j]
            i += 1
        
    print(nums)
    return i


print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([1,1,2,2,2,1]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))