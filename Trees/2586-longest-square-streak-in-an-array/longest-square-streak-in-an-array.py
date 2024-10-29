class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        streak = 0
        for n in hs:
            streak = 0
            # if int(math.sqrt(n)) not in hs:
            v = n
            while v in hs:
                streak += 1
                if v**2 > 10**5:
                    break
                v*=v

            res = max(res, streak)

        return res if res > 1 else -1
        