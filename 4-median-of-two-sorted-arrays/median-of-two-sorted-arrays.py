class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l = sorted(nums1 + nums2)

        length = len(l)
        median = (
            l[length // 2]
            if len(l) % 2 != 0
            else (l[int((length / 2) - 1)] + l[int((length / 2))]) / 2
        )

        return median
