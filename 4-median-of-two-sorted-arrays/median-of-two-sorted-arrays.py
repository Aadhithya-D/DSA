class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t = nums1+nums2
        t.sort()
        n = len(t)
        if n % 2 == 1:
            return t[n//2]
        elif n % 2 == 0:
            return ((t[n//2-1])+t[n//2])/2