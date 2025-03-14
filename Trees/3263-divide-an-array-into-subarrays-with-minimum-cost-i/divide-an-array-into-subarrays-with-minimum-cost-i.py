class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums.pop(0)

        second = min(nums)
        nums.remove(second)

        third = min(nums)
        nums.remove(third)

        return first + second + third