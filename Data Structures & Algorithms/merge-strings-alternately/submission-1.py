class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        if len(word1) > len(word2):
            return "".join(res + list(word1[len(word2):]))
        elif len(word2) > len(word1):
            return "".join(res + list(word2[len(word1):]))
        return "".join(res)