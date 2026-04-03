class TimeMap:

    def __init__(self):
        self.tMap = {} # each key maps to a list of values sorted by timestamp in asc order

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        if key not in self.tMap:
            self.tMap[key] = [] # must init a list if it doesn't exist, no way to do in init method
        self.tMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str: # O(log n)
        res = "" # default case where no valid value exists
        if key in self.tMap: # only do bsearch if key exists
            vals = self.tMap[key]
            l, r = 0, len(vals) - 1 # set up bsearch ptrs on value list at given key
            while l <= r:
                m = (l + r) // 2
                if vals[m][1] <= timestamp: # found a valid value, continue looking for better one
                    res = vals[m][0]
                    l = m + 1
                else:
                    r = m - 1
        
        return res