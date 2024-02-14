class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque([])
        good_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    good_oranges += 1

        temp_queue = deque([])
        counter = 0
        while queue:
            x, y = queue.popleft()
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for row, col in direction:
                new_row, new_col = row+x, col+y
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    temp_queue.append((new_row, new_col))
                    good_oranges -= 1
            if not queue and temp_queue:
                queue = temp_queue
                temp_queue = deque([])
                counter += 1
        return counter if good_oranges == 0 else -1