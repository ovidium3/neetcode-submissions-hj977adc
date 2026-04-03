class Solution: # O(n * m) time, O(n) mem
    def uniquePaths(self, m: int, n: int) -> int:
        # 2D DP approach - dont need a 2D table tho?
        # you can only move down or right - 2 choices so binary decision tree
        # notice how each time you move down or right, you can no longer reach a row or a column
        # define all values out of bounds as 0
        # table holds the unique ways from each position to reach the end result
        # since each row updates using the row below it, we dont even need a 2D array result - 1D works!
        # sounds like pascal's triangle - O(min(m, n)) time and O(1) space solution using math.comb(m + n - 2, m - 1)

        table = [1] * n # optimization since we build up one row at a time from the bottom row

        for i in range(m - 1): # start building from top right
            tempRow = table.copy() # same as initializing to [1] * n

            for j in range(n - 2, -1, -1): # avoid rightmost col, since that will always have a value of 1
                tempRow[j] = tempRow[j + 1] + table[j] # since table holds the old value of the row BELOW, j + 1 is val to the right

            table = tempRow # overwrite table with current row

        return table[0] # represents first column at the first row

        '''
        # pascal triangle solution
        return math.comb(m + n - 2, m - 1)
        '''