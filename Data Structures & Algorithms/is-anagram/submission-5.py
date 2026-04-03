class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)

        for k in counterS.keys():
            if counterS[k] != counterT[k]:
                return False
        return True if len(counterS) == len(counterT) else False