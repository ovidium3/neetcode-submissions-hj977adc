class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        max_int = 2**31 - 1
        min_int = -2**31

        while x:
            rem = int(math.fmod(x, 10)) # cannot mod bc negative numbers
            #print(rem)
            x = int(x / 10)
            
            if (res > max_int // 10 or # will overflow without needing to check last digit
                (res == max_int // 10 and rem >= max_int %10)): # all match but last, and will overflow
                return 0
            if (res < min_int // 10 or # all digits up to last are already at risk of overflowing
                (res == min_int // 10 and rem <= min_int % 10)):# will overflow from last digit alone, as all prev digits match
                return 0
            
            res *= 10
            res += rem

        return res