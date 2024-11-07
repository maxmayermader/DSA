class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def dfs(i, nums):
            if i == len(digits):
                res.append(nums)
                return
            
            for c in phone[digits[i]]:
                nums += c
                dfs(i+1, nums)
                nums = nums[0:-1]

        if not digits:
            return []
        dfs(0, "")
        return res 
