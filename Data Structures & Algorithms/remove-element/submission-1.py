class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        maxVal = max(nums)
        if val > maxVal:
            return len(nums)
        
        res = []

        rm = 0
        for i in range(len(nums)):
            if nums[i] != val:
                res.append(nums[i])
            else:
                rm += 1
        
        for i in range(len(res)):
            nums[i] = res[i]
        
        for i in range(rm):
            nums.pop()

        return len(nums)