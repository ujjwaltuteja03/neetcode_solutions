class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_amount = 0
        l = 0
        r = n - 1
        while l < r:
            l_height = heights[l]
            r_height = heights[r]
            curr_amount = min(l_height, r_height) * (r - l)
            if curr_amount > max_amount:
                max_amount = curr_amount
            if l_height > r_height:
                r -= 1
                while r_height >= heights[r] and l < r:
                    r -= 1
                
            else:
                l += 1
                while l_height >= heights[l] and l < r:
                    l += 1
        return max_amount