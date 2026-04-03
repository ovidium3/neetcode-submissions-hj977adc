class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= ROWS:
                return
            if c < 0 or c >= COLS:
                return     
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res