class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lst = []
#         flag = False
#         for i in nums:
#             for j in nums:
#                 print(i)
#                 print(j)
#                 print(nums.index(i))
#                 print(nums.index(j))
#                 print(i+j == target and nums.index(i) != nums.index(j))
#                 if i+j == target and nums.index(i) != nums.index(j):
#                     lst.append(nums.index(i))
#                     lst.append(nums.index(j))
#                     flag = True
                    
#                     print(nums.index(i))
#                     print(nums.index(j))
#                     break
#             if flag:
#                 break
        
#         #     if len(lst) > 1:
#         #         break
#         print(lst)
#         return lst
