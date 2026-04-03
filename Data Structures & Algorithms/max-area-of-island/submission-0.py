class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) # always track grid parameters first

        def findIsland(r: int, c: int) -> int: # set up dfs to find an entire island
            # base case
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            tile = grid[r][c]
            if not tile:
                return 0 # tile is either 0 (water) or 1 (land), so skip over water tiles
            
            # now handle island tiles - first remove it from existence and increment curr area
            grid[r][c] = 0

            return (1 + findIsland(r - 1, c)  # up
                      + findIsland(r + 1, c)  # down
                      + findIsland(r, c - 1)  # left
                      + findIsland(r, c + 1)) # right
        
        # brute force - check each tile but only if it is a land tile
        # optimization - turn land to water after checking, so you dont check the same island twice
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]: # only check land tiles
                    res = max(res, findIsland(r, c))
                
        return res