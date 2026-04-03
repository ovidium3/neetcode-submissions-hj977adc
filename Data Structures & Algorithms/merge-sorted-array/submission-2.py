class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

        p1, p2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if p2 < 0 or p1 < 0:
                break
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -=1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
        diff = abs(p2 - p1)
        if p2 > p1:
            for i in range(p2, -1, -1):
                nums1[i] = nums2[p2]
                p2 -= 1
