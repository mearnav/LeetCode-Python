class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        res = nums1 + nums2
        res1 = sorted(res)
        n = len(res1)

        mid = n // 2

        if n % 2 == 0:
            return ((res1[mid-1] + res1[mid]) / 2)
        else:
            return float(res1[mid])
            
