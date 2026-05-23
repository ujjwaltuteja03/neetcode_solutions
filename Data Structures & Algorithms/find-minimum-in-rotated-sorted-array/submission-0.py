class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        min=nums[0]
        for i in range(1, n):
            if nums[i] < min:
                min = nums[i]
        return min