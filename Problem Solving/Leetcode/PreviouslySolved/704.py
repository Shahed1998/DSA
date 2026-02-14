class Solution:
    def sequentialSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target: return i
            elif nums[i] > target: return -1

        return -1
    
    def BinarySearch(self, nums, target):
        front = 0
        rear = len(nums)-1

        while front <= rear:
            mid = front + (rear-front) // 2

            if nums[mid] == target: return mid

            elif nums[mid] < target: front = mid + 1

            elif nums[mid] > target: rear = mid - 1  

        return -1




sln = Solution()
print(sln.search([-1,0,3,5,9,12], 9))
print(sln.search([-1,0,3,5,9,12], 2))