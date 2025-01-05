class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def bfs(i, t):
            if i >= len(nums):
                return 1 if t == target else 0
            
            # if t == target:
            #     return 1

            if (i, t) in dp:
                return dp[(i, t)]

            dp[(i,t)] = bfs(i+1, t+nums[i]) + bfs(i+1, t-nums[i])
            return dp[(i,t)]

        return bfs(0, 0)
                