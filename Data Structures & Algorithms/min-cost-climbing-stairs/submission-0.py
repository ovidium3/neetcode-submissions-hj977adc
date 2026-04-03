class Solution: # O(n) time, O(1) space modifying cost array in-place
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # similar to other stair climbing - fibonacci sequence
        # top floor is one AFTER the last cost. can start at step 1 or 2.
        # modify cost array in-place, starting at idx 3, taking min of 1 or 2 jumps
        # brute force - using decision tree to break it down and draw it out
        # same as prev problem - dfs down one path in O(n) space OR tabulation approach
        
        for i in range(2, len(cost)): # avoid indexing out of bounds
            cost[i] += min(cost[i - 1], cost[i - 2]) # take shortest approach to get curr step
        
        return min(cost[-1], cost[-2]) # take min jump value to reach one past end of costs, which represents the last step