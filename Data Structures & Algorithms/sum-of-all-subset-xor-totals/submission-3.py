class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or1 = 0
        for i in nums:
            or1|=i
        return or1*(2**(len(nums)-1))