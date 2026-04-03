class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # by definition, k closest are all the entire array elts
        if k == len(arr):
            return arr

        # intuition: single pass can be done where we compare
        # the first elt and last to see which is closer match
        # and once we find that the first elt is clsoer than the last
        # in the sliding window, we can just return that slice of 
        # the array as teh result
        # we can do this by leveraging the sorting that is provided

        l, r = 0, k
        while r < len(arr):
            if x - arr[l] > arr[r] - x:
                r += 1
                l += 1
            else:
                break
        return arr[l:r]