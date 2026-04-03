class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for ch in s:
            sMap[ch] = 1 + sMap.get(ch, 0)

        for ch in t:
            tMap[ch] = 1 + tMap.get(ch, 0)

        for key in sMap:
            if sMap[key] != tMap.get(key, 0):
                return False

        return True