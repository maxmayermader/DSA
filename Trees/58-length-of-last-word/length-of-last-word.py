class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip().split(' ')
        print(res)
        return len(res[-1])
        