class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        mappings = collections.defaultdict()

        for i in intervals:
            start, end = i[0], i[1]
            intLen = end - start + 1
            for i in range(start, end + 1):
                if i in mappings:
                    mappings[i] = min(mappings[i], intLen)
                else:
                    mappings[i] = intLen
        
        res = []
        for q in queries:
            if q in mappings:
                res.append(mappings[q])
            else:
                res.append(-1)

        return res
