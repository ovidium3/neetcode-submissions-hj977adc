class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxMap = defaultdict(list)
        for i in range(len(nums)):
            idxMap[nums[i]].append(i)
        
        for v in idxMap.values():
            if len(v) < 2:
                continue
            for i in range(len(v) - 1):
                if abs(v[i] - v[i+1]) <= k:
                    return True
        return False