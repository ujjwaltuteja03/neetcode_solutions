class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1, n+1):
            if nums[i] == nums[i-1]: return nums[i]
        return -1