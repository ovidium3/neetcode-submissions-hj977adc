class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numStr = str()
        for num in digits:
            numStr += str(num)
        intNum = int(numStr)
        intNum += 1
        intNum = str(intNum)
        res = []
        for c in intNum:
            res.append(int(c))
        return res