class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]

            currMin = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    currMin = min(currMin, 1 + dfs(amount - coin ))
            dp[amount] = currMin
            return currMin 

        res = dfs(amount) 
        return res if res != float('inf') else -1
