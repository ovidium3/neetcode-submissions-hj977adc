class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: one permutation of empty list
        if not nums:
            return [[]]
        
        first = nums[0]
        rest = nums[1:]
        
        # Get permutations of the smaller problem
        smaller_perms = self.permute(rest)
        
        result = []
        
        # Build up permutations by inserting `first`
        for perm in smaller_perms:
            for pos in range(len(perm) + 1):
                
                new_perm = perm.copy()
                new_perm.insert(pos, first)
                
                result.append(new_perm)
        
        return result