class Solution: # O(n * m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # brute force naive way - dfs from each cell for O((n * m)^2) - pretty bad
        # correct way is to start from one side and try to reach the other, still doing dfs
        # but tracking which coords reach which side using two sets, one for each ocean
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set() # track which coords can reach. if (r, c) in both, add to res

        def dfs(r: int, c: int, prev: int, visited: set): # pass in either set, pacific or atlantic
            # base case
            if r not in range(ROWS) or c not in range(COLS):
                return
            curr = heights[r][c]
            if curr < prev or (r, c) in visited:
                return

            # add to visited and continue searching
            visited.add((r, c))
            dfs(r - 1, c, curr, visited) # up
            dfs(r + 1, c, curr, visited) # down
            dfs(r, c - 1, curr, visited) # left
            dfs(r, c + 1, curr, visited) # right

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0: # dfs from all top left edge pieces
                    dfs(r, c, 0, pacific)

                if r == ROWS - 1 or c == COLS - 1: # dfs from all bottom right edge pieces
                    dfs(r, c, 0, atlantic)

        res = [c for c in pacific if c in atlantic] # turn into a list only elts in both sets
        return res