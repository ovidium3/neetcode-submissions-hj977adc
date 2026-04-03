class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force solution = triple loop --> O(n^3)
        # optimal solution = sort input array and use 2 sum solution
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue # check prev val if it exists, to skip if duplicate
            
            # two sum implmentation
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res