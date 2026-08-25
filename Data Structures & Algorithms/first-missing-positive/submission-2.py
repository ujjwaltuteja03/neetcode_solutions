class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False]*n #boolean array
        for num in nums: 
            # the missing number has to be in the range 1 to n+1
            # for n sized array
            if num > 0 and num <= n:
                # mark all +ive numbers when seen
                # seen[num-1] since nth no. is at n-1 index

                seen[num-1] = True 
        for num in range(1, n+1):
            if not seen[num-1]:
                return num
        return n+1