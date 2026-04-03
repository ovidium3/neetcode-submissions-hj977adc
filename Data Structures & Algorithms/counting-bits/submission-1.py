class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        res = [0]
        powerOfTwo = 1

        for i in range(1, n + 1):
            if powerOfTwo * 2 == i:
                powerOfTwo *= 2
            dp[i] = 1 + dp[i - powerOfTwo]
            res.append(dp[i])

        return res

        # N log n solution
        # if n == 0:
        #     return [0]
        # if n == 1:
        #     return [0, 1]

        # res = [0, 1]
        # for i in range(2, n + 1):
        #     num = i
        #     ct = 0
        #     while num:
        #         num &= num - 1
        #         ct += 1
        #     res.append(ct)
        # return res