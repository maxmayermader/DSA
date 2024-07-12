# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         subset= []
#         def dfs(i):
#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return
#             subset.append(nums[i])
#             dfs(i+1)

#             subset.pop()
#             dfs(i+1)


#         dfs(0)
#         return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        
        def bt(i):
            nonlocal curr
            if i == len(nums):
                yield copy.deepcopy(curr)
                return
            curr.append(nums[i]) 
            yield from bt(i + 1)
            curr.pop()
            yield from bt(i + 1)
        return list(bt(0))            


