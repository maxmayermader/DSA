class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if  len(s) < k: # cannot have string longer than k. k=3 aa "a"+"a"+" " is invalid
            return False
        freq = Counter(s)
        oddCnt = 0 #count odds
        for key in freq:
            oddCnt += freq[key] %2
        return oddCnt <= k