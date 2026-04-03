class Solution: # O(m * n) time AND space
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # at first glance seems like a 2D matrix dfs problem
        # how to turn it into a DP array?
        # tricky because usually we only check down or right, this time we can check any 4 directions?
        # first code up DFS solution then try actual DP solution
        # have to process cells in ascending order, which requires nlogn sorting. faster to just DFS
        
        # memoization solution - more efficient timewise. although space comp is the same, can be worse due to recursion stack
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # map (r, c) to length of longest strictly increasing path from there
        
        currPath = set()
        def dfs(r: int, c: int, prev: int) -> int:
            # base cases
            if r not in range(ROWS) or c not in range(COLS): # row or col out of bounds
                return 0
            if (r, c) in currPath:
                return 0
            if matrix[r][c] <= prev: # violated constraint of strictly increasing
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            # else continue dfs in all four directions, finding longest path
            curr = matrix[r][c]
            cache[(r, c)] = (1 + max(dfs(r - 1, c, curr), # up
                            dfs(r + 1, c, curr), # down
                            dfs(r, c - 1, curr), # left
                            dfs(r, c + 1, curr))) # right
            return cache[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1) # cant start at 0, path must be strictly increasing
        
        return max(cache.values())