class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # best solution using bitmask for O(n) space
        ROWS, COLS = len(board), len(board[0]) # 9, 9
        
        rowBits = [0 for r in range(ROWS)]
        colBits = [0 for c in range(COLS)]
        squareBits = [0 for s in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == ".":
                    continue
                
                val = int(val)
                mask = 1 << val # bitshift number 1 val times
                                # producing e.g. 3 = ...01000
                if mask & rowBits[r]:
                    return False
                if mask & colBits[c]:
                    return False
                
                squareIdx = (r // 3) * 3 + (c // 3)
                if mask & squareBits[squareIdx]:
                    return False
                
                # OR bits so that it shows
                # e.g. 0010
                #    | 0100
                #    = 0110
                rowBits[r] |= mask
                colBits[c] |= mask
                squareBits[squareIdx] |= mask

        return True
        
        
        # # valid solution using sets, but this is O(n^2) space
        # ROWS, COLS = len(board), len(board[0]) # 9, 9
        
        # rowSets = [set() for r in range(ROWS)]
        # colSets = [set() for c in range(COLS)]
        # squareSets = [set() for s in range(9)]

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         val = board[r][c]
        #         if val == ".":
        #             continue
                
        #         if val in rowSets[r]:
        #             return False
        #         if val in colSets[c]:
        #             return False
                
        #         squareIdx = (r // 3) * 3 + (c // 3)
        #         if val in squareSets[squareIdx]:
        #             return False
                
        #         rowSets[r].add(val)
        #         colSets[c].add(val)
        #         squareSets[squareIdx].add(val)

        # return True
