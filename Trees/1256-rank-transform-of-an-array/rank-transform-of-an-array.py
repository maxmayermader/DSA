class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = [0]*len(arr)
        # temp 
        # arr.sort()
        # ranks = set(sorted(arr))
        ranks = {k: [] for k in sorted(set(arr))}
        for i,num in enumerate(arr):
            # ranks[num][0] = ranks[num][0] + 1
            ranks[num].append(i)

        print(ranks)
        # maxRank = 0
        # for key in ranks:
        #     maxRank = max(key, maxRank)

        
        # maxRankVal = len(ranks)
        # print(maxRankVal)
        # temp = sorted(arr)
        # print(temp)
        curRank = 1
        # j = len(res)
        for key in ranks:
            for i in ranks[key]:
                res[i] = curRank
            curRank += 1

        return res

        
        