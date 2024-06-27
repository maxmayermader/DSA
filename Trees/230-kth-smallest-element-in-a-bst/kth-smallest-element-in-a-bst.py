# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k-=1
            if 0 == k:
                return cur.val
            cur = cur.right
        
            

        # while root:
        #     if root.left:
        #         root = root.left
        #         stack.append(root)
        #     elif root.right:
        #         root = root.right
        #         stack.append(root)
        #         k+=1
        #     else:
        #         while k > 0:
        #             k -= 1
        #             if k == 0:
        #                 return stack.pop().val
        #             else:
        #                 stack.pop()
                    
                # return stack.pop().val

        
        