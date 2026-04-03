class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # intuition: we want to first find the midpoint
        # of the mountainArr so that we can then search both 
        # sides midpoints
        # OPTIMIZATION: dont need to know L and R to find peak
        # since we can only check if R is inc/decr compared to M


        mLen = mountainArr.length()
        l, r = 0, mLen - 1
        peak = 0 # peak of mountain Array
        while l <= r:
            m = l + (r - l) // 2
            mVal = mountainArr.get(m)
            rVal = mountainArr.get(m + 1)
            if mVal < rVal:
                # need to search right half
                l = m + 1
            else: # search left half
                r = m - 1
            peak = l

        l, r = 0, peak # include peak as maximum
        # of the left half of the array
        # search the left half of the mountain bsearch
        while l <= r:
            m = l + (r - l) // 2
            mVal = mountainArr.get(m)
            lVal = mountainArr.get(l)
            rVal = mountainArr.get(r)
            if mVal == target:
                return m
            elif mVal > target:
                # try searching left
                r = m - 1
            else:
                l = m + 1

        # still didnt find in left side, so now we can try
        # looking in the right half of the array
        l, r = peak, mLen - 1
        # search the right half of the mountain bsearch
        # but note that we kind of have the invariant flipped
        # i.e. sorted descending order
        while l <= r:
            m = l + (r - l) // 2
            mVal = mountainArr.get(m)
            lVal = mountainArr.get(l)
            rVal = mountainArr.get(r)
            if mVal == target:
                return m
            elif mVal > target:
                # actually want to search RIGHT half
                # since this is inversely sorted
                l = m + 1
            else:
                r = m - 1
        
        return -1