class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = collections.defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            freqMap[tuple(freq)].append(s)
        
        res = []
        for k, v in freqMap.items():
            res.append(v)
        return res
        
        # mapping = collections.defaultdict(list)
        # for s in strs:
        #     sSort = "".join(sorted(s))
        #     mapping[sSort].append(s)
        # res = []
        # for k, v in mapping.items():
        #     tmp = []
        #     res.append(v)
        # return res