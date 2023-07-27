import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # A min heap to store boundary heights

        # Add the boundary cells to the heap and mark them as visited
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        trapped_water = 0

        while heap:
            height, i, j = heapq.heappop(heap)

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    trapped_water += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = True

        return trapped_water