class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        idx,i,j=0,0,0
        for idx in range(len(nums1)):
            if j>=n or (i<m and temp[i]<=nums2[j]):
                nums1[idx] = temp[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j+=1
            