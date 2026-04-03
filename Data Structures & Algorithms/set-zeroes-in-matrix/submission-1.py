class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = set()
        colZero = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowZero.add(r)
                    colZero.add(c)
        
        for r in rowZero:
            matrix[r] = [0] * COLS
        for c in colZero:
            for r in range(ROWS):
                matrix[r][c] = 0
