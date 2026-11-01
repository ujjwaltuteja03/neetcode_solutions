class Solution:
    def bubble(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    def sortArray(self, nums: List[int]) -> List[int]:
            def bubble(arr):
                n = len(arr)
                for i in range(n):
                    swapped = False
                    for j in range(n-i-1):
                        if arr[j] > arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                            swapped = True
                    if not swapped:
                        break
                return arr
            res = bubble(nums)
            return res