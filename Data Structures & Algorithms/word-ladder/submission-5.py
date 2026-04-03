class Solution: # O(E^2) since we could have n^2 edges for n nodes
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # shortest path = use BFS. DFS used for all paths.
        # no need to do nested loop to build adj list
        # trick here is to add every variation of a word with a "*" to the adjacency list
        # where the * indicates the character that can be changed
        if endWord not in wordList: # edge case where word doesnt even exist
            return 0

        adjMap = defaultdict(list) # init dict as an empty mapping of str to list
        wordList.append(beginWord) # make sure we got this in here to then include it while iterating
        for word in wordList:
            for i in range(len(word)): # add every possible variation of word to adj map
                pattern = word[:i] + "*" + word[i + 1:]
                adjMap[pattern].append(word)

        transformations = 1 # start with 1 word as the base transformations required to get to end
        visited = set() # ensure you only bfs over each node once
        visited.add(beginWord)
        
        q = deque([beginWord]) # can just init like this, same with the set. that is done more for readability
        while q:
            for i in range(len(q)): # check entire current queue
                currWord = q.popleft()
                if currWord == endWord:
                    return transformations
                for j in range(len(currWord)):
                    pattern = currWord[:j] + "*" + currWord[j + 1:] # again check every variation
                    for word in adjMap[pattern]: # check all unvisited neighboring words in next q iteration
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
            transformations += 1

        return 0 # no more words left to search, so no solution