class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # positive diagonals all sum to the same value, negative diagonals subtract to the same value
        # create sets to keep track of cols, pos diags, and neg diags
        cols, posDiags, negDiags = set(), set(), set()


        res = []
        board = [["."] * n for i in range(n)] # create a board of default empty tiles (.)

        def backtrack(r: int) -> None: # only pass in row
            # base case - we found a valid board
            if r == n:
                copy = ["".join(row) for row in board] # have to join rows first to match output format
                res.append(copy)
                return
            
            for c in range(n):
                if (c not in cols and
                   (r + c) not in posDiags and
                   (r - c) not in negDiags): # only pursue valid solutions
                    # first have to update sets and mark queen
                    cols.add(c)
                    posDiags.add(r + c)
                    negDiags.add(r - c)
                    board[r][c] = "Q"

                    # now recursively call backtracking algo
                    backtrack(r + 1)

                    # now backtrack / undo after recursive call
                    cols.remove(c)
                    posDiags.remove(r + c)
                    negDiags.remove(r - c)
                    board[r][c] = "."
        
        backtrack(0)
        return res