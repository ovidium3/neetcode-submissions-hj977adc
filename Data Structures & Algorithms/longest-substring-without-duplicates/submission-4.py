class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        window = set()
        res = 0

        while r < len(s):
            if s[r] in window:
                res = max(res, len(window))
                while s[r] in window:
                    window.remove(s[l])
                    l += 1

            window.add(s[r])
            res = max(res, len(window))
            r += 1
        return res