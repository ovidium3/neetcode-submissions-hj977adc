class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)
        for s in strs:
            sSort = "".join(sorted(s))
            mapping[sSort].append(s)
        res = []
        for k, v in mapping.items():
            tmp = []
            res.append(v)
        return res