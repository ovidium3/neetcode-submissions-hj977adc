class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # can't have s1 be bigger than s2 for it to be a substr
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1 # need ordinal func to index correctly into 26 array
            counts2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)): # start at s1 len since already did that previously
            if matches == 26:
                return True

            # check right ptr and adjust match counts
            index = ord(s2[right]) - ord('a')
            counts2[index] += 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] + 1 == counts2[index]:
                matches -= 1
            
            # check left ptr and adjst match counts
            index = ord(s2[left]) - ord('a')
            counts2[index] -= 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] - 1 == counts2[index]:
                matches -= 1

            left += 1

        return matches == 26