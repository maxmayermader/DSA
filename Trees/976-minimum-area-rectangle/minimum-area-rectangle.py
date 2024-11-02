class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Convert points to set for O(1) lookup
        points_set = set(map(tuple, points))
        min_area = float('inf')
        n = len(points)
        
        # Check all possible pairs of points
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Skip if points are on same x or y coordinate
                if x1 == x2 or y1 == y2:
                    continue
                
                # Check if other two corners exist
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0