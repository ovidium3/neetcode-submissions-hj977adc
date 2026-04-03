class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCt = Counter(s)
        tCt = Counter(t)
        return sCt == tCt