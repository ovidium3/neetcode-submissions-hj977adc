class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set up two pointers, left and right at each side of the array
        lPtr = 0
        rPtr = len(nums) - 1

        while lPtr <= rPtr: # keep checking until they cross each other - then there is no solution
            mid = (lPtr + rPtr) // 2 # set up variable to represent "midpoint" number that you're checking

            if nums[mid] > target: # need to check left of current mid
                rPtr = mid - 1 # look to LEFT of midpoint so need to - 1
            elif nums[mid] < target: # need to check right of current mid
                lPtr = mid + 1 # look to RIGHT of midpoint so need to + 1
            elif nums[mid] == target: # found target, return index
                return mid

        return -1 # if you break out of loop, there is no solution so return -1