class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        hm = {}
        for num in nums:
            if num in hm:
                return True
            hm[num] = 1 + hm.get(num,0)


        return False