def removeDuplicates(nums):
    i = j = 0
    obj = {}

    for i in range(0, len(nums)):
        el = nums[i]

        if el not in obj:
            obj[el] = 1
            nums[j] = el
            j+=1
        i+=1

    # print(nums)
    return j



print(removeDuplicates([0,1,2,1,2,3,1,5]))

