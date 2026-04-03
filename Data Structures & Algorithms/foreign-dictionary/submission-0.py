class Solution: # O(number of chars)
    def foreignDictionary(self, words: List[str]) -> str:
        # topological sort - directed acyclical graph - build result in reverse order
        # edge case - prefix of a word comes before longer word
        # BFS and DFS solutions - DFS is better since less bookkeeping necessary
        # if we detect a cycle, it is invalid so return ""
        # if multiple solutions exist, all that matters is the char shows up before the next one in its order
        # workaround solution using DFS - postorder DFS where we add to output AFTER processing ALL descendants
        # create an adjacency list of each unique char mapping to a set of chars that come after it?
        adjList = { c:set() for w in words for c in w } # avoid duplicates and access faster than list
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # edge case where w1 is longer than w2 and they have the same prefix
                return "" # since this is an invalid ordering
            for j in range(minLen): # length of words to compare chars over
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j]) # 
                    break # stop looking at subsequent chars
        visited = {} # map char to bool. add with False to represent visited. change to True when in curr path.
        res = [] # join chars at the end in reverse order

        def dfs(c: str) -> bool: # python doesnt have chars so represent as str
            if c in visited:
                return visited[c] # if true we have a cycle, if false just visited
            
            visited[c] = True # now we can mark it as being in the current path

            for neighbor in adjList[c]:
                if dfs(neighbor):
                    return True # loop detected so just return

            visited[c] = False # after running DFS, no longer in curr path
            res.append(c)
        
        for c in adjList:
            if dfs(c):
                return "" # loop detected
        
        res.reverse()
        return "".join(res)