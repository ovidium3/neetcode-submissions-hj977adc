class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # follow up: no division use
        n = len(nums)

        prefixes = [0] * n
        prefixes[0] = nums[0]
        for i in range(1, n):
            prefixes[i] = prefixes[i - 1] * nums[i]
        
        suffixes = [0] * n
        suffixes[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i]

        # guaranteed nums len of at least 2
        for i in range(n):
            if i == 0:
                nums[i] = suffixes[i + 1]
            elif i == n - 1:
                nums[i] = prefixes[i - 1]
            else:
                nums[i] = prefixes[i - 1] * suffixes[i + 1]
        return nums


        # valid solution, but uses the division
        # zeroCt = 0
        # prod = 1
        # for i in range(len(nums)):
        #     n = nums[i]
        #     if n == 0:
        #         zeroCt += 1
        #     else:
        #         prod *= n
        # if zeroCt > 1:
        #     return [0] * len(nums)

        # for i in range(len(nums)):
        #     if nums[i] != 0 and zeroCt > 0:
        #         nums[i] = 0
        #     elif nums[i] == 0 and zeroCt > 1:
        #         nums[i] = 0
        #     elif nums[i] == 0 and zeroCt == 1:
        #         nums[i] = prod
        #     else: # nums[i] != 0 and zeroCt == 0
        #         nums[i] = prod // nums[i]
        # return nums