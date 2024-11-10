class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: #If sum is odd, partition impossible
            return False
        target = total //2
        dp = set() # Set of all possible sums
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            newDp = dp.copy() # Create new set to avoid modifying during iteration
            for v in dp:
                newDp.add(nums[i]+v)
                newDp.add(v)
            dp = newDp

        return target in dp

        
        
        