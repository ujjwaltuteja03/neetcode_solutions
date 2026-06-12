class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        secLast, last = 0,0

        for num in nums:
            temp = max(last, num+secLast)
            secLast=last
            last=temp
            
        return last