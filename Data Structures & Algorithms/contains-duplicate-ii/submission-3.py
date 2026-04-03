class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # optimal solution: sliding window set
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
        
        
        # # solution using hashmap O(n) time and space
        # idxMap = defaultdict(list)
        # for i in range(len(nums)):
        #     idxMap[nums[i]].append(i)
        
        # for v in idxMap.values():
        #     if len(v) < 2:
        #         continue
        #     for i in range(len(v) - 1):
        #         if abs(v[i] - v[i+1]) <= k:
        #             return True
        # return False