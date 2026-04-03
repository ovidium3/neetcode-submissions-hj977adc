class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0]) # 9, 9
        
        rowSets = [set() for r in range(ROWS)]
        colSets = [set() for c in range(COLS)]
        squareSets = [set() for s in range(9)]

        squareIdx = 0
        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in rowSets[r]:
                    return False
                if val in colSets[c]:
                    return False
                
                squareIdx = (r // 3) * 3 + (c // 3)
                if val in squareSets[squareIdx]:
                    return False
                
                rowSets[r].add(val)
                colSets[c].add(val)
                squareSets[squareIdx].add(val)

        return True
