class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        major = nums[0]
        for key in hm:
            if hm[key] > hm[major]:
                major = key

        return major
        