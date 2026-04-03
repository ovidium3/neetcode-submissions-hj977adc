class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) # to avoid confusion on calling len func
        
        # outer binary search loop O(log m)
        top, bottom = 0, ROWS - 1 # compute top and bottom row pointers
        while top <= bottom: # classic binary search while loop condition
            row = (top + bottom) // 2 # calculate current row midpoint
            if target > matrix[row][-1]: # check rightmost value using [-1]
                top = row + 1 # move up left pointer to one more than mid row
            elif target < matrix[row][0]: # check leftmost value using [0]
                bottom = row - 1 # move down right pointer to one less than mid row
            else: # target value is in the row so break
                break

        if top > bottom: # we did not "break" out of while loop as intended so there is no solution
            return False

        # inner binary search loop O(log n)
        lPtrInner, rPtrInner = 0, COLS - 1
        row = (top + bottom) // 2

        while lPtrInner <= rPtrInner: # keep checking until left pointer surpasses right
            midInner = (lPtrInner + rPtrInner) // 2 # calculate col midpoint

            if matrix[row][midInner] < target: # bring up left ptr to one more than mid
                lPtrInner = midInner + 1
            elif matrix[row][midInner] > target: # bring down right ptr to one less than mid
                rPtrInner = midInner - 1
            else: # target is equal so return true
                return True
        
        return False # exit while loop means no solution found so return -1