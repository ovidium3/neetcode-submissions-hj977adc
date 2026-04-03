class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            n = str(n)
            summed = 0
            for c in n:
                summed += int(c)**2
            if summed in seen:
                return False
            seen.add(summed)
            n = summed
        
        return True
