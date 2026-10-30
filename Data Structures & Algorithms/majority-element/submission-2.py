class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            if count == 0:
                maj = nums[i]
                count += 1
                continue
            elif nums[i] == maj:
                count += 1
            else:
                count -= 1
        return maj