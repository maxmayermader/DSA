class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [float('inf')]*len(prices)
        dp[0] = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            dp[i] = min(prices[i], dp[i-1])
            maxProfit = max(maxProfit, prices[i] - dp[i])

        return maxProfit
        