class Solution: # O(m * n), m = rows, n = cols
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # a DFS would be O((m * n)^2) but we can do better
        # run a BFS from all treasure chests outward, simultaneously
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647 # constant that represents infinity in this problem

        visited = set() # set of (r, c) to track visited tiles
        q = deque() # setup queue for bfs

        # first populate queue with treasure chest tiles ONLY
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        def addTile(r: int, c: int) -> None:
            if (r in range(ROWS) and c in range(COLS) and
                (r, c) not in visited and
                grid[r][c] != -1):
                visited.add((r, c))
                q.append([r, c])
                
        dist = 0 # distance to closest treasure. start at 0 bc treasure is 0 tiles away
        while q:
            for i in range(len(q)): # check one layer of queue at a time
                r, c = q.popleft()
                grid[r][c] = dist # update pos with distance from closest treasure

                # add all four adjacent tiles - create helper func to perform checks
                addTile(r - 1, c) # up
                addTile(r + 1, c) # down
                addTile(r, c - 1) # left
                addTile(r, c + 1) # right

            dist += 1 # increment distance to indicate moving on to next layer 