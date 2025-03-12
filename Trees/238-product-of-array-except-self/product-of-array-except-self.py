class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1]*N
        postfix = [1]*N
        
        # prefix[0] = nums[0]
        for i in range(1, N):
            prefix[i] = nums[i-1]*prefix[i-1]

        # postfix[N-1] = nums[N-1]
        for i in range(N-2, -1, -1):
            postfix[i] = postfix[i+1]*nums[i+1]

        print(prefix)
        print(postfix)

        nums[0] = postfix[0]
        nums[N-1] = prefix[N-2]
        for i in range(N):
            nums[i] = prefix[i] * postfix[i]

        return nums

