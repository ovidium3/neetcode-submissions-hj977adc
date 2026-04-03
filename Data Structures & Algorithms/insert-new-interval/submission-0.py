class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # pass thru intervals s.t. once new int start time is
        # leq curr interval end time, we go thru while all remaining
        # intervals start before newINt end?

        res = []

        curr = 0
        while curr < len(intervals):
            start, end = intervals[curr]
            newStart, newEnd = newInterval
            if newStart > end:
                res.append([start, end])
            elif newEnd < start:
                res.append([newStart, newEnd])
                res += intervals[curr:] # append rest of list
                return res
            else:
                # override newInt
                newInterval = [min(newStart, start), max(newEnd, end)]  
            curr += 1
        res.append(newInterval)           
        return res