class Solution: # O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # keep track of all subsets as they get completed

        subset = [] # current subset for each step of the problem
        def dfs(i): # i tells us which elt we're currently visiting
            if i >= len(nums): # check if we're out of bounds to stop recursion, no more leaf node
                finalSubset = subset.copy()
                res.append(finalSubset) # add final copy of current subset here
                return
            
            # left branch (decision to include nums[i])
            subset.append(nums[i])
            dfs(i + 1)

            # right branch (decision to NOT include nums[i])
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res