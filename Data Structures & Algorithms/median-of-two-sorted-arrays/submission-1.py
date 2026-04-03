class Solution: # O(log(min(n, m))) --> BETTER than O(log(n + m))!
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 # shorten var names to make it easier
        total = len(A) + len(B) # total length (m + n)
        half = total // 2 # median index in **combined** array pos

        if len(A) > len(B): # swap to make A the smaller array since we only bsearch on 1 array
            A, B = B, A

        l, r = 0, len(A) - 1 # don't forget the -1 index out of bound error! also A is shorter array

        while True: # keep looping - will eventually find midpoint
            i = (l + r) // 2 # A's midpoint
            j = half - i - 2 # B's midpoint - we have to do -2 instead of just -1 to avoid idx error

            # setting up infinity's (+ and -) for A and B arrays
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # case where partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # if total % 2 == 1 means it is odd
                    return min(Aright, Bright)
                # else it must be even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # max of L partition, min of R partition
            elif Aleft > Bright: # case where A is too big, need to reduce size of A
                r = i - 1
            else: # case where A is too small, need to increase
                l = i + 1
