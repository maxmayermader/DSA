# class Solution:
#     def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
#         colors = [0]*n
#         adj = set()
#         pairCount = 0
#         res = []
#         for i,c in queries:
#             colors[i] = c
#             pairs = 0
#             if i in adj or i+1 in adj or i - 1 in adj:
#                 if i - 1 > 0 and colors[i-1]

#             res.append(pairCount)

#         return res

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        ans, d, cnt = [], defaultdict(int), 0

        for i, color in queries:

            if d[i]: cnt-= (d[i-1] == d[i])+(d[i+1] == d[i])
            d[i] = color
            if d[i]: cnt+= (d[i-1] == d[i])+(d[i+1] == d[i])

            ans.append(cnt)

        return ans