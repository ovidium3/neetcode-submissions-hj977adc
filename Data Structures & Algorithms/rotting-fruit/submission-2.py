class Solution: # O(m * n), visit each node once using BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # run a bfs from each rotten fruit outwards
        # every iteration, go through current q and add new fresh fruits that touch rotten
        # no need to keep track of visited tiles, since once we convert a fresh fruit to rotten,
        # there's no way it could pass the check of being a fresh fruit again.
        # if fresh fruit remain, return -1 else return number of times q has been iterated over
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        self.fresh = 0 # make it global to access in helper func
        
        # start q off with all rotten fruit, and count number of fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    self.fresh += 1

        def addTile(r: int, c: int) -> None:
            if (r in range(ROWS) and c in range(COLS) and # index must be in range
                grid[r][c] == 1): # tile must contain a fresh fruit
                q.append([r, c]) # add to q
                grid[r][c] = 2 # mark fruit as rotten
                self.fresh -= 1 # decr fruit count
        
        # iterate through q, one layer at a time, until no more fresh fruit can be contaminated
        time = 0
        while q and self.fresh: # can stop early once all fresh fruit have been contaminated to avoid over-decrementing
            for i in range(len(q)):
                r, c = q.popleft()
                
                # call helper to avoid duplicate checks, and mark tiles as visited + add to next level queue
                addTile(r - 1, c) # up
                addTile(r + 1, c) # down
                addTile(r, c - 1) # left
                addTile(r, c + 1) # right
            
            time += 1 # increment time to go to next level of bfs
        
        return time if self.fresh == 0 else -1 # return time to took to rot all, or -1 if not possible