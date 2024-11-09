class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:  # If sum is odd, partition impossible
            return False
        
        target = total // 2
        dp = set([0])  # Set of all possible sums
        
        for num in nums:
            next_dp = dp.copy()  # Create new set to avoid modifying during iteration
            for t in dp:
                next_dp.add(t + num)
            dp = next_dp
            
        return target in dp
        