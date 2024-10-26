class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # hm with end char and end time
        # loop through s
        # last occurence of visited chars is the end of s
        hm = {}
        for i,c in enumerate(s):
            hm[c] = i

        res = []
        maxEnd = 0
        cnt = 1
        for i in range(len(s)):
            maxEnd = max(maxEnd, hm[s[i]])
            if i == maxEnd:
                res.append(cnt)
                cnt = 0
            cnt += 1

        return res
# ababcbaca d e. f
# 012345678 9 10 11