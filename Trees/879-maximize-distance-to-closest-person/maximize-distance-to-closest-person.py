class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev = -1
        maxDist = 0
        
        for i in range(n):
            if seats[i] == 1:
                # Handle distance from start if no person at beginning
                if prev == -1:
                    maxDist = i
                else:
                    # Calculate distance between two people
                    maxDist = max(maxDist, (i - prev) // 2)
                prev = i
        
        # Handle distance to end if no person at end
        if prev != n - 1:
            maxDist = max(maxDist, n - 1 - prev)
            
        return maxDist

            