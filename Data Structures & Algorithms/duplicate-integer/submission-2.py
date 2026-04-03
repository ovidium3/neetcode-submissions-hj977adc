class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        processed = set()
        for num in nums:
            if num in processed:
                return True
            processed.add(num)
        return False