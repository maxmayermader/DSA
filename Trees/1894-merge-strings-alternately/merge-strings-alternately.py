class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = ""

        while p1 < len(word1) and p2 < len(word2):
            if p1 > p2:
                res += word2[p2]                
                p2 += 1
            elif p2 > p1:
                res += word1[p1]
                p1 +=1
            else:
                res += word1[p1]
                p1 +=1
        
        if len(word1) > p1:
            res += word1[p1:]

        if len(word2) > p2:
            res += word2[p2:]

        print(res)
        return res        