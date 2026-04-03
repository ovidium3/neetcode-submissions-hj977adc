"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key = lambda x:x.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if start >= rooms[0]:
                heapq.heappop(rooms)  
            heapq.heappush(rooms, end)

        return len(rooms)