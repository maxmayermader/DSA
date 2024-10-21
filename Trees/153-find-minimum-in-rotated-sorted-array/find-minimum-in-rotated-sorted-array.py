class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minNum = float('inf')
        while l <= r:
            m = (l + r) // 2
            minNum = min(minNum, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min(minNum, nums[0])












        # def binSearch(l, r):
        #     m = (r + l) // 2
        #     if l >= r:
        #         return nums[m]

        #     if l > -1 and r < len(nums):
        #         return min(nums[m], min(binSearch(m+1, r), binSearch(l, m-1)))

        # return binSearch(0, len(nums)-1)