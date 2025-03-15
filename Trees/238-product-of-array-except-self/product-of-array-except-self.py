class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        pre = 1
        for i in range(N):
            res[i] = pre
            pre *= nums[i]
        suff = 1
        for i in range(N-1, -1, -1):
            res[i] *= suff
            suff *= nums[i]
        return res
        