class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        n = len(prices)
        # Initialize dp array properly for each day and state
        dp = [[0] * 2 for _ in range(n + 1)]
        
        # Iterate backwards through the prices
        for cur in range(n - 1, -1, -1):
            # State 0: Not holding stock
            dp[cur][0] = max(
                dp[cur + 1][1] - prices[cur],  # Buy
                dp[cur + 1][0]                 # Skip
            )
            
            # State 1: Holding stock
            dp[cur][1] = max(
                dp[cur + 1][0] + prices[cur],  # Sell
                dp[cur + 1][1]                 # Skip
            )
            
        return dp[0][0]
        

"""
Case 1: Not holding a stack
        a. buy
        b. skip
Case 2: Holding a stock
        a. sell a stock for profit
        b. skip
"""