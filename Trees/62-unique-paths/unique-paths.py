class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(m-1, n-1) : 1} # (r, c) : move count
        directions = [[0, -1], [-1, 0]]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                for dr, dc in directions:
                    newr, newc = r + dr, c + dc
                    if newr >= 0 and newc >= 0:
                        if (newr, newc) in dp:
                            dp[(newr, newc)] +=  dp.get((r,c), 0)
                        else:
                            dp[(newr, newc)] =  dp.get((r,c), 0)


        return dp[(0,0)]
        