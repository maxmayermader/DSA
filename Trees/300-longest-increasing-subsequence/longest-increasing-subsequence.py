class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 0

        for i in range(len(nums)-1, -1, -1):
            r = i + 1
            currMax = 0
            while r < len(nums):
                if nums[i] < nums[r]:
                    currMax = max(currMax, dp[r])
                r+=1
            dp[i] += currMax
            res = max(res, dp[i])

        return res
                
        