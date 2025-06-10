# Time complexity - O(n), and Space complexity - O(1), Apply Moore's voting algorithm,
# In Moore's voting algorithm, the majority element must be more than N/2 times

def majorityElement(nums):

    if len(nums) < 1: return nums
    
    candidate, count = nums[0], 1

    for i in range(1, len(nums)):

        if count == 0:
            candidate = nums[i]

        if nums[i] == candidate:
            count += 1
        else:
            count -= 1

        
    return candidate


# print(majorityElement([3,2,3]))
# print(majorityElement([2,2,1,1,1,1,1,2,2])) 
# print(majorityElement([1,1,1,1,1,1,1])) 
print(majorityElement([1,1,1,1,2,2,3,3])) 