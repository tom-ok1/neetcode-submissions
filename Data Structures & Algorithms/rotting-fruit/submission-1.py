from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in dirs:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))

            minutes += 1

            if fresh == 0:
                return minutes

        return -1