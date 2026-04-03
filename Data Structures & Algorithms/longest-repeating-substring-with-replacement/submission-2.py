class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        charCounts = {}

        left = 0
        # maxf = 0
        for right in range(len(s)):
            charCounts[s[right]] = 1 + charCounts.get(s[right], 0)
            # maxf = max(maxf, count[s[right]])

            if (right - left + 1) - max(charCounts.values()) > k:
            # if (right - left + 1) - maxf > k:
                charCounts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest