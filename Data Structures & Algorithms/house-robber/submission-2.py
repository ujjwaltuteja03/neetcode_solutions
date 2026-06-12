class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob1 is house i-2, rob2 is house i-1
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2