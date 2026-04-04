class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force: use a hash set to store all
        # seen numbers and if we encounter dupe --> return it
        seen = set()
        
        for n in nums:
            if n in seen:
                return n
            seen.add(n)