class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # attempt at best: use nums as a hash map
        # first loop: neutralize negative numbers
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # second loop: track which nums appear in sequence
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums): # within bounds
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1 # negate to indicate presence
                elif nums[val - 1] == 0: # edge case
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        # third loop: tally up nums in array and see
        # what the lowest missing val is
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i # missing in the input array
        return len(nums) + 1 # worst case: all nums 1 to len(nums) + 1 present

        
        
        # # slightly better: O(n) time set solution
        # nSet = set()
        # for n in nums:
        #     if n > 0:
        #         nSet.add(n)
        # minPos = min(nSet) if nSet else 1
        # if minPos > 1:
        #     return 1
        # # else minPos == 1
        # while minPos in nSet:
        #     minPos += 1
        # return minPos

        
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