class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 4.2B
        max_int = 0x7FFFFFFF # 2.1B

        # bit shift carry if we have to add two 1's
        # mask in case of negative nums, which would convert
        # to a very large int potentially
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        if a <= max_int:# to check if we need to flip all bits
        # in the case of a negativ enumebr
            return a
        return ~(a ^ mask)
