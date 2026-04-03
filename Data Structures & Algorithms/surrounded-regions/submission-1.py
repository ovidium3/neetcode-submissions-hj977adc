class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # scan entire border, looking for o's
        # once we find an o, run dfs to find all connected o's, and mark those coords
        # then, turn the rest of the board to x's EXCEPT the marked coords
        ROWS, COLS = len(board), len(board[0])
        bordering = set() # track all bordering 'o' tiles

        def dfs(r: int, c: int):
            # base case
            if r not in range(ROWS) or c not in range(COLS): # index out of range
                return
            tile = board[r][c]
            if tile == "X" or (r, c) in bordering: # only connect o's that havent been processed already
                return
            
            bordering.add((r, c))
            
            # keep searching for o's
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

        for r in range(ROWS):
            for c in range(COLS):
                if ((r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and
                    board[r][c] == "O"): # bordering tile that is also an 'o'
                    dfs(r, c) # run dfs to mark entire connected component

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in bordering:
                    board[r][c] = "X" # change non bordering o tiles to x's