class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def select(arr):
            n = len(arr)
            for i in range(n-1):
                min_i= i
                for j in range(i+1, n):
                    if arr[j] < arr[min_i]:
                        min_i = j
                arr[i], arr[min_i] = arr[min_i], arr[i]
            return arr
        res = select(nums)
        return res