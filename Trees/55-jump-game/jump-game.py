class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


        # i = nums[0]
        # while nums[0] > 0:
        #     j = i
        #     while j < len(nums):
                
        #         if nums[j] == nums[-1]:
        #             return True
        #         temp = nums[j]
        #         nums[j] -= 1
        #         j += temp
        #     nums[0] -= 1


        # return False

        