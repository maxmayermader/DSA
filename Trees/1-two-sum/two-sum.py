class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                return [hm[nums[i]], i]
            else:
                hm[target-nums[i]] = i