class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #zeroIdxs = [False] * len(nums)
        zeroCt = 0
        prod = 1
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                #zeroIdxs[i] = True
                zeroCt += 1
            else:
                prod *= n
        for i in range(len(nums)):
            if nums[i] != 0 and zeroCt > 0:
                nums[i] = 0
            elif nums[i] == 0 and zeroCt > 1:
                nums[i] = 0
            elif nums[i] == 0 and zeroCt == 1:
                nums[i] = prod
            else: # nums[i] != 0 and zeroCt == 0
                nums[i] = prod // nums[i]
        return nums