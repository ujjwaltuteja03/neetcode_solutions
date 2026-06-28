class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged= nums1+nums2
        merged.sort()
        totalL=len(merged)
        if totalL%2==0:
            return (merged[totalL//2-1]+merged[totalL//2])/2.0
        else:
            return merged[totalL//2]