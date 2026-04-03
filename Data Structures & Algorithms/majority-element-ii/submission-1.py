class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # candidates
        first = None
        second = None
        firstCt = 0
        secondCt = 0

        # 1st pass: find candidates
        for num in nums:
            if first == num:
                firstCt += 1
            elif second == num:
                secondCt += 1
            elif firstCt == 0:
                first = num
                firstCt = 1
            elif secondCt == 0:
                second = num
                secondCt = 1
            else:
                firstCt -= 1
                secondCt -= 1

        # 2nd pass: verify counts
        res = []
        firstCt = secondCt = 0

        for num in nums:
            if num == first:
                firstCt += 1
            elif num == second:
                secondCt += 1

        n = len(nums)
        if firstCt > n // 3:
            res.append(first)
        if secondCt > n // 3:
            res.append(second)

        return res
            
        
        
        # # simple solution: counter to store all elts O(n) time + space
        # numCts = Counter(nums)
        # res = []
        # for k, v in numCts.items():
        #     if v > len(nums) // 3:
        #         res.append(k)
        # return res