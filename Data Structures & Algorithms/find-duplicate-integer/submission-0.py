class Solution: # O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        need to recognize that 1) this is a LinkedList problem AND 2) Floyd's Tortoise and Hare algo
        this works because 2 * slow = fast
        after finding the intersection point between slow and fast
        set up another slow ptr and once that intersects the first slow ptr, that is the result
        mathematically proven that the distance between starting node and result intersection is
        equivalent to the distance between the first intersection and the result intersection
        '''
        
        # step 1: find first intersection point in cycle
        slow, fast = nums[0], nums[nums[0]] # start at 0 since we know 0 is not part of the cycle
        while slow != fast:
            slow = nums[slow] # acts as a pointer incremented once
            fast = nums[nums[fast]] # somehow acts as a pointer that is incremented twice

        # step 2: find second intersection point (result)
        slowStart = 0
        while slow != slowStart:
            slow = nums[slow]
            slowStart = nums[slowStart]

        return slow # after we break out of while loop this pointer will represent the correct index