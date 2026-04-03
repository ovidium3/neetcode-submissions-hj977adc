class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neigh = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neigh[pattern].append(word)

        bfs = deque([beginWord])
        visited = set()#[beginWord])
        ct = 1
        while bfs:
            for i in range(len(bfs)):
                curr = bfs.popleft()
                visited.add(curr)
                if curr == endWord:
                    return ct
                
                for j in range(len(curr)):
                    pattern = curr[:j] + "*" + curr[j + 1:]
                    for w in neigh[pattern]:
                        if w not in visited:
                            bfs.append(w)
                            #visited.add(w)
            ct += 1

        return 0
