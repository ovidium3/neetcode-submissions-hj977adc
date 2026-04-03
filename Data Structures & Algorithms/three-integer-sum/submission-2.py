class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # optimal solution: sort and reduce to 
        # multiple twoSum problems
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
        
        listRes = []
        for tup in res:
            listRes.append(list(tup))
        return listRes