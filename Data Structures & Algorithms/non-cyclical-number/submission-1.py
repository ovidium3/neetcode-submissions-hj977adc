class Solution:
    def isHappy(self, n: int) -> bool:
        def cycle(n: int):
            n = str(n)
            summed = 0
            for c in n:
                summed += int(c)**2
            return summed

        slow, fast = n, cycle(n)
        while slow != fast:
            slow = cycle(slow)
            fast = cycle(cycle(fast))
        
        return fast == 1
