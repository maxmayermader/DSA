class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[-float('inf')]*2]*len(prices)
        
        @lru_cache(maxsize=None)
        def dfs(cur, hold):
            if cur == len(prices):
                return 0
            
            ch1, ch2 = 0, 0
            if hold is 1:
                ch1 = dfs(cur+1, 0) + prices[cur]
                ch2 = dfs(cur+1, 1)
            else:
                ch1 = dfs(cur+1, 1) - prices[cur]
                ch2 = dfs(cur+1, 0)
            return max(ch1, ch2)

        return dfs(0, 0)
        

"""
Case 1: Not holding a stack
        a. buy
        b. skip
Case 2: Holding a stock
        a. sell a stock for profit
        b. skip
"""