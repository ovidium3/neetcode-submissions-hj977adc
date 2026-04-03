class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= ROWS:
                return 0
            if c < 0 or c >= COLS:
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res