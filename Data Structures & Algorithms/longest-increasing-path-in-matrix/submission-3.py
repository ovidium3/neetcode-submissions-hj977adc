class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])

        cache = [[-1] * M for _ in range(N)]

        def dfs(x, y, prev):
            if x < 0 or x >= N:
                return 0
            if y < 0 or y >= M:
                return 0
            if (x, y) in visited:
                return 0
            visited.add((r, c))
            if matrix[x][y] > prev:
                prev = matrix[x][y]
            else:
                return 0

            if cache[x][y] != -1:
                return cache[x][y]
            cache[x][y] = 1 + max(dfs(x - 1, y, prev), dfs(x + 1, y, prev), dfs(x, y + 1, prev), dfs(x, y - 1, prev))
            return cache[x][y]

        res = 1
        for r in range(N):
            for c in range(M):
                visited = set()
                res = max(dfs(r, c, -1), res)
        return res