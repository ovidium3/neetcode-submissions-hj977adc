class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # constant space solution: 
        # if we know that all nums are within range
        # of 1 to n, then we can just treat them as
        # pointers and a linked list that has a cycle
        # therefore we can use Floyd two pointer slow/fast
        # approach? hard to figure out
        # think of each number as pointing to a specific index
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # MORE: you need to then start a SECOND slow
        # pointer to find the TRUE start of the cycle,
        # NOT jsut the intersection point!
        # key invariant: the intersection point is the same as 
        # the distance between the start and the detection point
        # WHY? algebra. 2 * slow = fast
        # 2 (P + C - X) = P + 2C - x --> P - X = 0 --> P = X
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        # brute force: use a hash set to store all
        # seen numbers and if we encounter dupe --> return it
        # seen = set()
        
        # for n in nums:
        #     if n in seen:
        #         return n
        #     seen.add(n)