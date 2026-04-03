class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # define a dfs function to find entire island, and once it is done identifying all pieces,
        # increment result. key = turn all found islands into water to avoid double counting
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def findIsland(r: int, c: int) -> bool:
            # base cases
            if r not in range(ROWS) or c not in range(COLS):
                return False
            tile = grid[r][c]
            if tile == "0":
                return False
            
            # now handle island pieces - first remove island, then check all around it for any more
            grid[r][c] = "0"

            findIsland(r - 1, c) # up
            findIsland(r + 1, c) # down
            findIsland(r, c - 1) # left
            findIsland(r, c + 1) # right
        
            # DO NOT backtrack by restoring island in grid pos

        for r in range(ROWS):
            for c in range(COLS):
                tile = grid[r][c]
                if tile == "1":
                    res += 1
                findIsland(r, c) # recursively identify entire island + remove it from grid

        return res