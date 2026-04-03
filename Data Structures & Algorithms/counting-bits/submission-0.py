class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        res = [0, 1]
        for i in range(2, n + 1):
            num = i
            ct = 0
            while num:
                num &= num - 1
                ct += 1
            res.append(ct)
        return res