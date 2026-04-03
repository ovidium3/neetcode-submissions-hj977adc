class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # better solution: sliding window where we start out with
        # a hashmap of size window and keep updating it as we
        # iterate across the string in one pass, checking it against
        # the initial counter of s1? as opposed to constructing a new
        # one every time?     
        # can hyper optimize to only check match count (i.e. 26 chars and freqs)
        # but this is good   
        
        # brute force: check all possible substring lengths
        # for possible inclusion using hashmap of s1
        cts = Counter(s1)

        l, r = 0, len(s1) - 1
        curr = s2[l : r + 1]
        currCt = Counter(curr)
        while r < len(s2):
            if cts == currCt:
                return True
            currCt[s2[l]] -= 1
            l += 1
            r += 1
            if r == len(s2):
                return False
            currCt[s2[r]] += 1
        return False