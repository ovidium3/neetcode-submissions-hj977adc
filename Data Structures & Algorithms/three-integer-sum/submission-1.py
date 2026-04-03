class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        nums.sort()
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] + nums[i] == 0:
                    tup = [nums[i], nums[lo], nums[hi]]
                    res.add(tuple(tup))
                    hi -= 1
                    lo += 1
                elif nums[lo] + nums[hi] + nums[i] > 0:
                    hi -= 1
                elif nums[lo] + nums[hi] + nums[i] < 0:
                    lo += 1

            # for j in range(i + 1, len(nums)):
            #     for k in range(j + 1, len(nums)):
            #         if nums[i] + nums[j] + nums[k] == 0:
            #             tup = [nums[i], nums[j], nums[k]]
            #             res.add(tuple(tup))
        
        listRes = []
        for tup in res:
            listRes.append(list(tup))
        return listRes