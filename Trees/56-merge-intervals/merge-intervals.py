class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start, end])

        return res

            


        


        # newInterval = []
        #     if intervals[i][1] >= intervals[i+1][0]:
        #         newInterval = [intervals[i][0], intervals[i+1][1]]
        #         res.apeend(newInterval)
        #     else: