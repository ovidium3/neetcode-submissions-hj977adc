"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # intuition: what even is this
        # 1. if the current grid has the same value
        # i.e. all 1's or all 0's, set isLeaf True and set
        # val to the value of the grid and set the four children
        # to null and stop
        # 2. if the current grid has different vals, set isLeaf
        # to False and set val to any value and divide the
        # current grid into four sub-grids
        # 3. recurse for each of the children with the proper subgrid
        ROWS = COLS = len(grid)
        totalVals = 0
        for g in grid:
            totalVals += sum(g)
        
        # BASE CASE: set isLeaf True, set val to val of grid, 
        # set children null + stop
        if totalVals == 0 or totalVals == (ROWS * COLS):
            val = grid[0][0]
            return Node(val, True, None, None, None, None)
        
        # set isLeaf to false and set val to any value
        # and divide curr grid into four subgrids
        topLeft = []
        topRight = []
        bottomLeft = []
        bottomRight = []
        mid = ROWS / 2
        for r in range(ROWS):
            L = []
            R = []
            for c in range(COLS):
                if c < mid: # add to L
                    L.append(grid[r][c])
                else: # add to R
                    R.append(grid[r][c])
            if r < mid:
                topLeft.append(L)
                topRight.append(R)
            else:
                bottomLeft.append(L)
                bottomRight.append(R)

        tL = self.construct(topLeft)
        tR = self.construct(topRight)
        bL = self.construct(bottomLeft)
        bR = self.construct(bottomRight)

        return Node(grid[0][0], False, tL, tR, bL, bR)
