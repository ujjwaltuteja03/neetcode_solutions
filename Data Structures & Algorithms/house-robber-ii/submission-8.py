class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)
        
        def take(nums):
            one, two = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp = two 
                two = max(nums[i] + one, two)
                one = temp
            return two
        
        return max(take(nums[:-1]), take(nums[1:]))