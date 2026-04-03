class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # intuition: we can bsearch like we did in the prev
        # problem to find the min element, and if we do
        # not find the number within range then we can
        # just return False
        # NOTE: we must handle duplicates i.e. we cannot
        # just say if nums[m] > target go right
        # worst case O(n) since we can possibly increment
        # l by 1 if we have array where l and r are equal values
        # since we dont know where the array cutoff point is

        l, r = 0, len(nums) - 1
        while l <= r:
            # meh way:
            # m = (l + r) // 2
            # better way:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            elif nums[m] > nums[l]: # left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]: # right portion
                if nums[m] <= target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False