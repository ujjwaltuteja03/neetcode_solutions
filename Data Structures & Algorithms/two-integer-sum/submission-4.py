class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res =[]
        Seen = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in Seen:
                return [Seen[diff], i]
            Seen[n] = i