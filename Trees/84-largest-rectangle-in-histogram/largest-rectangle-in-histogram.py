class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, currh in enumerate(heights):
            start = i
            while stack and  stack[-1][1] > currh:
                index, sheight = stack.pop()
                res = max(res, sheight*(i - index))
                start = index
            stack.append((start, currh))
            # if stack[-1][1] <= currh:
            #     stack.append((i, currh))
            # else:
            #     index, sheight = stack.pop()
            #     res = max(res, sheight*(i - index))
            #     while sheight > currh:
            #         index, sheight = stack.pop()
            #         res = max(res, height*(i - index))
            #     stack.append((index, currh))

        while stack:
           index, sheight = stack.pop()
           res = max(res, sheight*(len(heights)-index)) 


        return res
            
                