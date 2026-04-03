class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # slightly better: O(n) time set solution
        nSet = set()
        for n in nums:
            if n > 0:
                nSet.add(n)
        minPos = min(nSet) if nSet else 1
        if minPos > 1:
            return 1
        # else minPos == 1
        while minPos in nSet:
            minPos += 1
        return minPos

        
        # # O(nlogn) brute force sort
        # nums.sort()
        # curr = 0
        # for n in nums:
        #     if n < 1:
        #         continue
        #     if n - curr == 0:
        #         continue
        #     if n - curr == 1:
        #         curr += 1
        #     else:
        #         return curr + 1
        # return curr + 1