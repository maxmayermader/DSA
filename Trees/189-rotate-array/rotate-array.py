class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        def rev(l, r):
            while l < r:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
                r -= 1

        rev(0, N-1)
        rev(0, k-1)
        rev(k, N-1)


        