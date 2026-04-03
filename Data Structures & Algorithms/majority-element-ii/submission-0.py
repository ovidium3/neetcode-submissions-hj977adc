class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # simple solution: counter to store all elts O(n) time + space
        numCts = Counter(nums)
        res = []
        for k, v in numCts.items():
            if v > len(nums) // 3:
                res.append(k)
        return res