class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i, c in enumerate(s):
            hm[c] = i

        res = []
        end = hm[s[0]]
        size = 0
        for i in range(len(s)):
            
            end = max(end, hm[s[i]])
            size+=1
            if i == end:
                res.append(size)
                size = 0

        return res