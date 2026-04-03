class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        res = 0
        total = 0
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]
            total += g - c
            if total < 0:
                total = 0
                res = i + 1

        return res