class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda x:x[0])

        res = []

        prev = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = prev[0], prev[1]
            if start <= prevEnd:
                prev = [min(start, prevStart), max(end, prevEnd)]
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res
