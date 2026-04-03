class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixes = [[0] * (len(matrix[0]) + 1) for r in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            currSum = 0
            for c in range(len(matrix[0])):
                currSum += matrix[r][c]
                self.prefixes[r + 1][c + 1] = currSum + self.prefixes[r][c + 1]
        print(self.prefixes) 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixes[row2 + 1][col2 + 1] - self.prefixes[row2 + 1][col1] - self.prefixes[row1][col2 + 1] + self.prefixes[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)