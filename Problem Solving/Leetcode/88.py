def merge(nums1, m: int, nums2, n: int):
    i = m
    j = 0

    while(i < len(nums1)):
        nums1[i] = nums2[j]
        i += 1
        j += 1
    
    nums1.sort()

    print(nums1)
    print(nums2)
        

merge([1,2,3,0,0,0], 3, [2,5,6], 3)