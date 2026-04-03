class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # intuition: we can just track the curr max val
        # and the next val we see in the array
        # and compare that to see if we need to add
        # the curr max val or the new max when we expadn
        # the array using a hashmap
        # optimization: use a heap for nlogn or deque for O(n)

        l, r = 0, k - 1
        window = deque()
        for i in range(k):
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
        res = []
        res.append(nums[window[0]])
        l += 1
        r += 1

        while r < len(nums):
            if window[0] < l:
                window.popleft()

            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)
            res.append(nums[window[0]])
            r += 1
            l += 1
        return res
        