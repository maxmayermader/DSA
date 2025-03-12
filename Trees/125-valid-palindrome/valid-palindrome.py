class Solution:
    def isPalindrome(self, s: str) -> bool:
        s0 = []
        for c in s:
            if c.isalnum():
                s0.append(c.lower())

        l = 0 
        r = len(s0)-1

        while l < r:
            if s0[l] != s0[r]:
                return False
            l += 1
            r -= 1

        return True
        