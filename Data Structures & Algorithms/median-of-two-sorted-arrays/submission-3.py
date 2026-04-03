class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # intuition: we want to partition the arrays
        # such that we have two equal halves and that
        # then we can just take the largest val in the left
        # most half, and the smallest val in the right
        # most half and return the computation of those
        # e.g.: [1, 3, 5]
        #.      [2, 4, 6]
        # -->   1, 3] [5
        #.      2] [4, 6
        # == max(left) + min(right) / 2 since even
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1 # reassign arrays to make
            # the smaller one always nums1

        l, r = 0, len(nums1) - 1
        while True:
            m1 = l + (r - l) // 2
            m2 = half - m1 - 2 # since both indices start at 0, -1 -1 == -2

            # if midpoint is out of bounds, we want 
            l1 = nums1[m1] if m1 >= 0 else float("-infinity")
            r1 = nums1[m1 + 1] if m1 + 1 < len(nums1) else float("infinity")
            l2 = nums2[m2] if m2 >= 0 else float("-infinity")
            r2 = nums2[m2 + 1] if m2 + 1 < len(nums2) else float("infinity")

            # partition invariant is correct:
            # element in smaller array leftmost val is
            # leq right most element in larger array
            # AND left most element in larger array 
            # leq right most element in smaller array
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    # odd case
                    return min(r1, r2)
                else: # even case
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = m1 - 1
            else:
                l = m1 + 1
