class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0

        for i in range(len(num1)):
            for j in range(len(num2)):
                mult = int(num1[i]) * int(num2[j])
                
                # total at this position
                total = res[i + j] + mult

                # split into digit + carry
                digit = total % 10
                carry = total // 10

                # write back
                res[i + j] = digit
                res[i + j + 1] += carry
        
        while res[-1] == 0:
            res.pop()
        s = ""
        for n in res[::-1]:
            s += str(n)
        return s