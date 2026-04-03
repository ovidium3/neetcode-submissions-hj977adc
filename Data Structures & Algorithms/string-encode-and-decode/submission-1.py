class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for st in strs:
            res += str(len(st))
            res += "#"  # delimiter makes it easier
            res += st

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        sPtr = 0
        while sPtr < len(s):
            delimPtr = sPtr
            while s[delimPtr] != "#":
                delimPtr += 1

            strLen = int(s[sPtr:delimPtr]) # need this to avoid improper use of delimeter ptr
            sPtr = delimPtr + 1
            delimPtr = sPtr + strLen
            res.append(s[sPtr:delimPtr])
            sPtr = delimPtr # move up string ptr

        return res
