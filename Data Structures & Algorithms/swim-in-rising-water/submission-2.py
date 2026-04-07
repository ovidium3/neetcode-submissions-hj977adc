class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # intuition: we keep trying to dfs from the farthest 
        # position we reach until we eventually can hit the last 
        # r,c pos in the grid!
        # we can optimize by tracking the farthest index 
        # we have made it to but that might be a bit too complex for now
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, height):
            if r < 0 or r == ROWS:
                return False
            if c < 0 or c == COLS:
                return False
            if grid[r][c] > height:
                return False
            if grid[r][c] in visited:
                return False

            if r == ROWS - 1 and c == COLS - 1:
                return True
            
            visited.add(grid[r][c])
            
            return dfs(r - 1, c, height) or dfs(r + 1, c, height) or dfs(r, c + 1, height) or dfs(r, c - 1, height)


        time = 0
        while True:
            visited = set()
            if dfs(0, 0, time):
                return time
            time += 1
