class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        # aan | naa 
        # elle
        # el b le
        # for a string to be palindrome all charecters must have an even count and at most one charecter can have an odd count
        if  len(s) < k: # cannot have string longer than k. k=3 aa "a"+"a"+" " is invalid
            return False
        freq = Counter(s)
        oddCnt = 0 #count odds
        for key in freq:
            oddCnt += 1 if freq[key] %2 != 0 else 0
        return oddCnt <= k
        
        if oddCnt > k: # How many malindromes we have to make to account for odd charecters
            return False
        return True
        
        numPalindromes = (len(freq) - oddCnt) 
        return numPalindromes == k
