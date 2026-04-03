class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        
        nums1back = m + n - 1
        nums1mid = m - 1
        nums2back = n - 1

        while nums2back >= 0:
            if nums1mid >= 0 and nums1[nums1mid] >= nums2[nums2back]:
                nums1[nums1back] = nums1[nums1mid]
                nums1mid -= 1
            else:
                nums1[nums1back] = nums2[nums2back]
                nums2back -= 1
            nums1back -= 1