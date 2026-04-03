class Solution: # O(log n)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # set up l and r ptrs for bsearch

        while l <= r:
            m = (l + r) // 2 # calculate midpt
            
            if nums[m] == target: # case where target matches (easy)
                return m # just return index
            elif nums[l] <= nums[m]: # we're in left sorted portion. <= since Lvalue could be equal
                if target > nums[m] or target < nums[l]: # cases 1 and 2 - move up left ptr
                    l = m + 1
                else: # case 3 - move down right ptr
                    r = m - 1
            else: # we're in right sorted portion
                if target < nums[m] or target > nums[r]: # cases 1 and 2 - move down right ptr same idea as above
                    r = m - 1
                else: # case 3 - only have to search right portion of the array
                    l = m + 1

        return -1