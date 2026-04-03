class Solution: # O(n^2 * n!) == O(n!) time and O(n! * n) == O(n!) space
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) == 0:
            return [[]] # empty list
        
        perms = self.permute(nums[1:]) # recursively call but remove first elt
        res = []

        for perm in perms:
            for i in range(len(perm) + 1): # find every possible index we could insert that first value in
                permCopy = perm.copy()
                permCopy.insert(i, nums[0])
                res.append(permCopy)

        return res

        '''
        can also do it without recursion: same time and space complexity btw
        perms = [[]]
        
        for n in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    newPerms.append(pCopy)
            perms = newPerms
        return perms
        '''