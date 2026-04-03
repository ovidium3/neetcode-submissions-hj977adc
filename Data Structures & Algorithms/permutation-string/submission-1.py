class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force: check all possible substring lengths
        # for possible inclusion using hashmap of s1
        cts = Counter(s1)

        l, r = 0, len(s1) - 1
        while r < len(s2):
            curr = s2[l:r + 1]
            print(curr)
            currCt = Counter(curr)
            if cts == currCt:
                return True
            l, r = l + 1, r + 1
        return False