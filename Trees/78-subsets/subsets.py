class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        # # res = []
        # def backtrack(first=0, curr=[]):
        #     if len(curr) == k:
        #         res.append(curr[:])
        #         return
        #     for i in range(first, n):
        #         curr.append(nums[i])
        #         backtrack(i+1, curr)
        #         curr.pop()

        # res = []
        # n = len(nums)
        # for k in range(n+1):
        #     backtrack()
        # return res

        