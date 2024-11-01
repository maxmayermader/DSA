class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dirs = [(-1,1), (0,1), (1,1)]
        maxMoves = 0
        
        def bfs(start):
            moves = -1
            visit = set()
            q = deque()
            q.append(start)
            visit.add(start)  # Add initial position to visited set

            while q:
                qlen = len(q)
                for _ in range(qlen):
                    r, c = q.popleft()

                    for dr, dc in dirs:
                        newr, newc = r + dr, c + dc
                        if (0 <= newr < len(grid) and 
                            0 <= newc < len(grid[0]) and 
                            grid[newr][newc] > grid[r][c] and 
                            (newr, newc) not in visit):
                            q.append((newr, newc))
                            visit.add((newr, newc))
                moves += 1
            
            return max(0, moves)  # Return 0 if no moves possible

        for i in range(len(grid)):
            maxMoves = max(maxMoves, bfs((i, 0)))

        return maxMoves