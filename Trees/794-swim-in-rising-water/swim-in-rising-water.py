class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW = len(grid)-1
        COL = len(grid[0])-1
        directions=[[0,1], [0,-1], [1,0], [-1, 0]]

        pq = [(grid[0][0], 0, 0)]
        visit = set([(0, 0)])  # Add the starting cell to visited set

        while pq:
            cost, r, c = heapq.heappop(pq)

            if r == ROW and c == COL:
                return cost

            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                if (0 <= newR <= ROW and
                    0 <= newC <= COL and
                    (newR, newC) not in visit):
                    
                    visit.add((newR, newC))  # Mark as visited before adding to queue
                    newCost = max(cost, grid[newR][newC])
                    heapq.heappush(pq, (newCost, newR, newC))

        return -1  # In case no path is found (shouldn't happen for valid inputs)
        