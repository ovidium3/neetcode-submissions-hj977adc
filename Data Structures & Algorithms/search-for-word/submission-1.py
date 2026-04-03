class Solution: # O(n * m * dfs) - dfs = 4^len(word)
    def exist(self, board: List[List[str]], word: str) -> bool:
        # could just brute force and check each tile, doing backtracking recursively (dfs)
        ROWS, COLS = len(board), len(board[0])
        path = set() # keep track of positions that we already visited

        def dfs(r, c, i): # nested func to avoid passing in board and word vars
            # base cases
            if i == len(word): # we found the word
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or # row or col indexed out of board bounds
                word[i] != board[r][c] or (r, c) in path): # letter doesnt match or is already in path
                return False

            # leaves us with correct letter in the word, so keep checking all possible locations
            path.add((r, c))
            res = (dfs(r - 1, c, i + 1) or # up
                   dfs(r + 1, c, i + 1) or # down
                   dfs(r, c - 1, i + 1) or # left
                   dfs(r, c + 1, i + 1))   # right
            
            path.remove((r, c)) # reset path in case prev one didnt work and you need to try again later
            return res
        
        # brute force - check each tile to run dfs
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False