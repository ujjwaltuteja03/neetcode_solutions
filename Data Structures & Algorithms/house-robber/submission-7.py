class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        one = nums[0]
        two = max(nums[0], nums[1])
        if n == 2:
            return two
        i = 2
        while i<n:
            temp = two
            two = max(one+nums[i], two)
            one = temp
            i+=1
        return two