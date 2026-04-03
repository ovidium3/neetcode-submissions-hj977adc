class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        
        ptr = hi // 2
        while hi > lo:
            if target > nums[ptr]:
                lo = ptr + 1 # avoid duplicate checking
            elif target < nums[ptr]:
                hi = ptr
            else: # match!
                return ptr
            ptr = (hi + lo) // 2
        
        return -1