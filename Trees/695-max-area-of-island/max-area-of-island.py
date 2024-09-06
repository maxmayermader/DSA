class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(start):
            q = deque()
            q.append(start)
            visited.add(start)
            islandSize = 1

            while q:
                r, c = q.popleft()
                adj = []
                
                # for i in range(-1,2):
                #     if i != 0 and r + i >= 0 and r + i < ROWS:
                #         adj.append((r+i, c))
                # for j in range(-1,2):
                #     if j != 0 and c + j >= 0 and c + j < COLS:
                #         adj.append((r, c+j))
                # for nr, nc in adj:
                #     if grid[nr][nc] != 0 and (nr, nc) not in visited:
                #         q.append((nr, nc))
                #         visited.add((nr, nc))
                #         islandSize += 1
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4-directional movement

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        islandSize += 1
               

            return islandSize

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != 0 and (i,j) not in visited:
                    res = max(res, bfs((i,j)))

        return res
                        

            
