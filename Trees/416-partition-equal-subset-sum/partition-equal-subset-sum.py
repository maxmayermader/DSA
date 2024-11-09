class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        cache = {}
        
        def dfs(i, currSum):
            if i >= len(nums) or currSum > target:
                return currSum == target
                
            if (i, currSum) in cache:
                return cache[(i, currSum)]
                
            cache[(i, currSum)] = (
                dfs(i + 1, currSum) or 
                dfs(i + 1, currSum + nums[i])
            )
            return cache[(i, currSum)]
        
        return dfs(0, 0)
        