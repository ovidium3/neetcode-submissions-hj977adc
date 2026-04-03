class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lPtr = 0
        rPtr = len(nums) - 1

        while lPtr <= rPtr:
            mPtr = (lPtr + rPtr) // 2
            
            if nums[mPtr] > target:
                rPtr = mPtr - 1
            
            elif nums[mPtr] < target:
                lPtr = mPtr + 1

            else:
                return mPtr

        return -1