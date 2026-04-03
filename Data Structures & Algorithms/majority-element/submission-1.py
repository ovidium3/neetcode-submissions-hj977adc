class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nCt = Counter(nums)
        maxCt = 0
        maxVal = 0
        for k, v in nCt.items():
            if v > maxCt:
                maxCt = v
                maxVal = k
        return maxVal