class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # greedy partitioning - we can go until we hit a repeat char
        # then we need to ensure all chars up to last pos
        # is in the curr substr
        counts = Counter(s)
        seen = set()
        currChars = 0
        res = []
        currLen = 0

        for c in s:
            currLen += 1
            
            if c not in seen:
                seen.add(c)
                currChars += 1
            
            counts[c] -= 1
            
            if counts[c] == 0:
                currChars -= 1
            
            # finished partitioning all instances of chars
            if currChars == 0:
                res.append(currLen)
                currLen = 0
                seen.clear()

        return res