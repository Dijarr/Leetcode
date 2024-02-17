class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque()
        fresh, time = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for row, col in directions:
                    newRol, newCol = row+r, col+c
                    if 0 <= newRol < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRol][newCol] == 1:
                        grid[newRol][newCol] = 2
                        queue.append((newRol, newCol))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                




