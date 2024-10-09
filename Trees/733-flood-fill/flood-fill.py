class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        prev = image[sr][sc]
        if prev == color:
            return image
        q.append((sr, sc))
        visit = set()
        # visit.add((sr, sc))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()
            if (r,c) in visit:
                continue
            visit.add((r, c))
            image[r][c] = color
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if (newR, newC) not in visit and 0 <= newR < len(image) and 0 <= newC < len(image[0]) and image[newR][newC] == prev:
                    q.append((newR, newC))
                    

        return image
            
