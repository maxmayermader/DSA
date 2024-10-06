class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm1 = {}
        hm2 = {}

        for c in s:
            hm1[c] = 1 + hm1.get(c, 0)

        for c in t:
            hm2[c] = 1 + hm2.get(c, 0)

        for c in t:
            if c not in hm1 or hm1[c] != hm2[c]:
                return False

        return True
        