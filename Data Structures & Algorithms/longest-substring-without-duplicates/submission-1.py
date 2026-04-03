class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        currSeq = set()

        left = 0
        for right in range(len(s)):
            while s[right] in currSeq:
                currSeq.remove(s[left])
                left += 1
            currSeq.add(s[right])
            longest = max(longest, right - left + 1) # take maximum of curr longest seq and prev longest
                
        return longest