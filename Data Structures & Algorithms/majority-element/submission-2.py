class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res

        # threshold = (len(nums) // 2) + 1
        # nCt = Counter(nums)
        # maxCt = 0
        # maxVal = 0
        # for k, v in nCt.items():
        #     if v > maxCt:
        #         maxCt = v
        #         maxVal = k
        # return maxVal