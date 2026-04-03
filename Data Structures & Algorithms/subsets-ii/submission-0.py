class Solution: # O(n * 2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # not dynamic programming since we have to create the subsets, not just count them
        # decision tree - include element, or skip ALL duplicates
        # have to sort in order to skip all duplicates! sorting is only nlogn so no big deal
        # time complexity is upper bound - we prune duplicates so typically wont be as bad.
        res = [[]] # init res with empty list as that is auto subset
        nums.sort()
 
        curr = [] # init sublist
        def dfs(i):
            if i >= len(nums): # no more elts left to consider
                return
            
            num = nums[i]

            # left subtree - include elt and go on to the next regardless of duplicate
            curr.append(num)
            res.append(curr.copy())
            dfs(i + 1)

            # right subtree - dont include elt AND skip over all duplicates
            curr.pop()
            while i < len(nums) and nums[i] == num:
                i += 1
            dfs(i)
        
        dfs(0)
        return res