class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if r < 0 or r == ROWS:
                return False
            if c < 0 or c == COLS:
                return False
            if board[r][c] != word[i]:
                return False
            if (r, c) in visited:
                return False
            visited.add((r, c))
            if i == len(word) - 1:
                return True

            res = dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
            visited.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, 0):
                        return True
        return False