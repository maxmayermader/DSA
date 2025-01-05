class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} #(index, target at that point)

        def bfs(i, t):
            if i >= len(coins) or t > amount: # no more coins or total exceeds amount
                return 0

            if t == amount:
                return 1
            
            if (i, t) in dp:
                return dp[(i,t)]

            dp[(i,t)] = 0  # Initialize before adding combinations
            # Use current coin multiple times or skip to next coin
            dp[(i,t)] = bfs(i, t + coins[i]) + bfs(i + 1, t)

            return dp[(i,t)]

        return bfs(0,0)

