class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        res = 0
                    
        def bfs(start):
            q = deque()
            q.append(start)
            visited.add(start)
            while q:
                curr = q.popleft()
                adj= []
                for i in range(-1,2):
                    if i != 0:
                        if curr[0]+i >= 0 and curr[0]+i < ROWS:
                            adj.append((curr[0]+i,curr[1]))

                for j in range(-1,2):
                    if j != 0:
                        if  curr[1]+j >= 0 and curr[1]+j < COLS:
                            adj.append((curr[0],curr[1]+j))

                for cord in adj:
                    if cord not in visited and grid[cord[0]][cord[1]] != "0":
                        q.append(cord)
                        visited.add(cord)


            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs((i,j))
                    res+=1

        
        return res