# class Solution:
#     def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
#         good = set()

#         for t in triplets:
#             if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
#                 continue
            
#             for i, v in enumerate(t):
#                 if v == target[i]:
#                     good.add(i)

#         return len(good) == 3

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #triplets.sort()
        a,b,c = 0,0,0
        for i in range(len(triplets)):
            if(triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]):
                a = max(a,triplets[i][0])
                b = max(b,triplets[i][1])
                c = max(c,triplets[i][2])
            if a==target[0] and b==target[1] and c==target[2]:
                return True
        return False