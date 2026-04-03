class Solution: # O(V + E)^2 since potential backtracking -> O(E^2) time, O(E) mem
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use DFS since all paths are same length, but compare lexicographically
        # create an adjacency list as well to conduct DFS on
        adjList = defaultdict(list)
        for src, dst in tickets:
            adjList[src].append(dst)
        for src in adjList:
            adjList[src].sort() # process lexicographically smallest first

        path = [] # init path with jfk since they all start there
        def dfs(src: str) -> None:
            # base case - lexicographically smallest output complete, stop searching for more solutions
            if len(path) > len(tickets):
                return
            # go through entire adjacency list to keep adding to path
            while adjList[src]:
                dfs(adjList[src].pop(0)) # pop from front to process smallest first
            path.append(src)
        
        dfs("JFK") # init path as jfk
        path.reverse() # since we pop from the back and sorted smallest first
        return path