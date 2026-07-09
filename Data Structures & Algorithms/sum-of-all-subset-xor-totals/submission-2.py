class Solution:
    # brute force recursion
    # including and excluding an element at each step 
    # leads to forming 2^n subsets of an array
    # include: dfs(i+1, total^nums[i])
    # exclude:dfs(i+1, nums[i])

    # TC: O(2^n), SC: O(n)
     
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total
            return dfs( i+1, total^nums[i]) + dfs(i+1, total)
        return dfs(0,0)