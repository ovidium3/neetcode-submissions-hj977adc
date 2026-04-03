class TimeMap:
    # we can try to do log n retrieval for get, where
    # n == the length of the duplicate entries for
    # a specific key

    def __init__(self):
        self.m = defaultdict(list) # store val, timestamp pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.m[key]
        if len(vals) == 0:
            return ""
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + (r - l) // 2 # to avoid possibel overflow
            val, time = vals[m]
            if time <= timestamp:
                l = m + 1
            elif time > timestamp:
                r = m - 1
            else: # time == timestamp
                return val
        return vals[r][0] if r >= 0 else ""
