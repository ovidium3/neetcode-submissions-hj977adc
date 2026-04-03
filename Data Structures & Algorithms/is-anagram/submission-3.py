class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for ch in s:
            if ch not in sMap:
                sMap[ch] = 1
            else:
                sMap[ch] += 1
            # alternatively use the .get method: with default value of zero: .get(ch, 0)

        for ch in t:
            if ch not in tMap:
                tMap[ch] = 1
            else:
                tMap[ch] += 1

        for k, v in sMap.items():
            if k not in tMap:
                return False
            elif k in tMap and tMap[k] != sMap[k]:
                return False

        return True