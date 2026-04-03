class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        sList.sort()
        tList = list(t)
        tList.sort()
        if sList == tList:
            return True
        return False