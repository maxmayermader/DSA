class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBanana = 1
        minBanana = 1
        for banana in piles:
            maxBanana = max(maxBanana, banana)
        res = 0
        while minBanana <= maxBanana:
            k = (maxBanana + minBanana)// 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile)/k)
            if time <= h:
                res = k
                maxBanana = k -1
            else:
                minBanana = k + 1
        return res