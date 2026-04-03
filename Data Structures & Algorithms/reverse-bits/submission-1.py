class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))
        n = n[2:]
        #remaining = 32 - len(n)
        #n += remaining * "0"
        n = n[::-1]
        print(n)

        res = 0
        val = 2**31
        for i in range(len(n)):
            if n[i] == "1":
                res += val
            val //= 2
        return res
        #return int(n)