class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 4.2B
        max_int = 0x7FFFFFFF # 2.1B

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        if a <= max_int:
            return a
        return ~(a ^ mask)
