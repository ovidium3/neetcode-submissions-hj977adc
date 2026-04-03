class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0,0,0]
        for t in range(len(triplets)):
            if curr == target:
                return True
            a, b, c = triplets[t]
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            curr = [max(a, curr[0]), max(b, curr[1]), max(c, curr[2])]
            # print(curr)
        return curr == target#False