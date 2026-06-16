class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        Min, Max= 1, 1
        for num in nums:
            tmp = Max*num
            Max= max(tmp, num*Min, num)
            Min= min(num, tmp, num*Min)
            res= max(res, Max)
        return res