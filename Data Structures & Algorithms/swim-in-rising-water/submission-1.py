class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find max elt in path is what it sounds like
        # keep adding numbers in asc order until we have a path
        # how to check that a path is complete? visited set
        # union find until the top left square is in the same
        # connected component as the bottom right square
        # PQ approach with dijkstra's tends to be more efficient in practice
        # just push back the running total height into the PQ so u can directly return
        
        ROWS = COLS = len(grid) # define constants
        SIZE = ROWS * COLS # it is a square

        visited = set() # contains (r, c)

        def check(r: int, c: int, height: int) -> None:
            if (r in range(ROWS) and c in range(COLS) and
                (r, c) not in visited): # add valid tiles to PQ
                visited.add((r, c))
                height = max(height, grid[r][c]) # update max height
                heapq.heappush(pq, [height, r, c])

        pq = [[grid[0][0], 0, 0]] # sorted by value, row, col
        while pq:
            height, row, col = heapq.heappop(pq)
            if row == ROWS - 1 and col == COLS - 1: # we reached the last square
                return height
            # else keep checking tiles
            check(row - 1, col, height)
            check(row + 1, col, height)
            check(row, col - 1, height)
            check(row, col + 1, height)
            
        '''
        # DOESNT WORK
        SIZE = len(grid) ** 2 # since it is a square
        ROWS = COLS = len(grid) # since 0-indexed
        parent = [ i for i in range(SIZE) ] # represents each node's ancestor
        rank = [1] * SIZE # represents size of each ancestor node's connected component

        def find(node) -> int: # returns node's highest ancestor, compressing path along the way
            curr = node # make copy of current node to avoid modification issues
            while curr != parent[curr]: # while there is no more parent to go up to
                parent[curr] = parent[parent[curr]] # set curr parent straight to grandparent, if it exists
                curr = parent[curr] # move up one after compressing path
            return curr # should now point to the highest ancestor

        def union(node1, node2) -> bool:
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2: # already in same connected component
                return False
            
            if rank[parent1] > rank[parent2]: # add parent2 component size to parent1
                rank[parent1] += rank[parent2] # add value of parent2 component
                rank[parent2] = 0 # update value of parent2 component size to 0
            else: # append parent1 component to parent2
                rank[parent2] += rank[parent1]
                rank[parent1] = 0
            return True # successfully performed union
        
        valCoords = {} # map value to coords where it lies
        for r in range(ROWS):
            for c in range(COLS):
                valCoords[grid[r][c]] = (r, c)

        for i in range(SIZE):
            union(0, i)
            if not union(0, grid[ROWS - 1][COLS - 1]):
                return i # always gonna be most recently added
        '''