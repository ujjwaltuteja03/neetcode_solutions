class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for total in range(1, target+1):
            dp[total] = 0
            for num in nums:
                # to reach a value total, each num first needs 
                # to be able to reach total-num (which is 0 for -ive nums)
                dp[total] += dp.get(total-num,0)
        return dp[target]