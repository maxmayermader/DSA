class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
                
            # if nums[m] < target:
            #     if nums[r] < nums[m]:
            #         r = m - 1
            #     else:
            #         l = m + 1
            # else:
            #     if nums[l] > nums[r]:
            #         l = m + 1
            #     else:
            #         r = m - 1


        return -1