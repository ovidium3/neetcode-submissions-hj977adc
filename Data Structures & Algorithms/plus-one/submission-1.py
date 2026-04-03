class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for d in digits[::-1]:
            d += carry
            if d == 10:
                carry = 1
                res.append(0)
            else:
                carry = 0
                res.append(d)
        if carry:
            res.append(1)
        return res[::-1]