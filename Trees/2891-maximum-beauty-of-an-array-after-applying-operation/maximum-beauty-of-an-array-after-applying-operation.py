class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxCnt = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1

            maxCnt = max(maxCnt, r-l+1)
            # if nums[r] - nums[l] <= 2 * k:
            #     cnt += 1
            #     maxCnt = max(maxCnt, cnt)

            # else:
            #     maxCnt = max(maxCnt, cnt)
            #     cnt = 0

        return maxCnt