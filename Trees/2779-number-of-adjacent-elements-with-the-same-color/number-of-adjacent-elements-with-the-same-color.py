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
        colors = n*[0]
        answer = []
        curanswer = 0
        for query in queries:
            index = query[0]
            oldcolor = colors[index]
            colors[index] = query[1]
            if index > 0:
                if(colors[index-1] == oldcolor and oldcolor != 0):
                    curanswer -= 1
                if(colors[index-1] == query[1]):
                    curanswer += 1
            if index < n-1:
                if(colors[index+1] == oldcolor and oldcolor != 0):
                    curanswer -= 1
                if(colors[index+1] == query[1]):
                    curanswer += 1
            answer.append(curanswer)
        return answer