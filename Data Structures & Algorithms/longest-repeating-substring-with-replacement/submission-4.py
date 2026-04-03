class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        
        l, r = 0, 0
        res = 0
        while r < len(s):
            freqs[s[r]] += 1
            mostFreq = max(freqs.values())
            
            while sum(freqs.values()) - mostFreq > k:
                freqs[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return res