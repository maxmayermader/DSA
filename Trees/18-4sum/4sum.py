class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums: List[int], target: int, start: int, end: int) -> List[List[int]]:
            res = []
            left, right = start, end
            
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            return res
        
        n = len(nums)
        if n < 4:
            return []
            
        nums.sort()
        result = []
        
        for i in range(n-3):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, n-2):
                # Skip duplicates for second number
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                # Find remaining two numbers using two pointers
                remainingTarget = target - nums[i] - nums[j]
                for pair in twoSum(nums, remainingTarget, j+1, n-1):
                    result.append([nums[i], nums[j]] + pair)
        
        return result