class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        
        # Base case: when we reach the end
        dp[n][0] = dp[n][1] = 0
        
        # Iterate backwards through the array
        for i in range(n - 1, -1, -1):
            # Not holding a stock
            dp[i][0] = max(
                dp[i + 1][1] - prices[i],  # buy
                dp[i + 1][0]               # skip
            )
            
            # Holding a stock
            dp[i][1] = max(
                dp[i + 1][0] + prices[i],  # sell
                dp[i + 1][1]               # skip
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