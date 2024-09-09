class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                            rooms[nr][nc] != -1 and 
                            (nr, nc) not in visited):
                            
                            q.append((nr, nc))
                            visited.add((nr, nc))
                rooms[r][c] = dist
            dist +=1

        