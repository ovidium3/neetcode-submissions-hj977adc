class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))
        n = n[2:] # remove 0b
        n = n[::-1]# reverse

        res = 0
        val = 2**31
        # build backwards
        for i in range(len(n)):
            if n[i] == "1":
                res += val
            val //= 2
        return res