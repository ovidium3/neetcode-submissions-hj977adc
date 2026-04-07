class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # intuition: we keep trying to dfs from the farthest 
        # position we reach until we eventually can hit the last 
        # r,c pos in the grid!
        # we can optimize by tracking the farthest index 
        # we have made it to but that might be a bit too complex for now
        # OR we can run binary search? but on what parameter of T?
        # min and max of the grid!
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

        timeL = timeR = 0
        for r in range(ROWS):
            timeL = min(timeL, min(grid[r]))
            timeR = max(timeR, max(grid[r]))

        while timeL <= timeR:
            visited = set() # guaranteed each pos is unique
            time = (timeL + timeR) // 2
            if dfs(0, 0, time):
                # COULD solve this with curr height
                # constraint, try to narrow it down a bit
                timeR = time - 1
            else: # try larger time
                timeL = time + 1
        return timeL