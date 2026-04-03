class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1]) # sort by start

        res = 0
        recent_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < recent_end:
                res += 1
                recent_end = min(end, recent_end)
            else:
                recent_end = end
        return res