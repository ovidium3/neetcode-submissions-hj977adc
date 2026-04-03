class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        maxVal = max(nums)
        if val > maxVal:
            return len(nums)

        valid = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[valid] = nums[i]
                valid += 1

        return valid