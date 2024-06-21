# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


        # pStack = []
        # qStack = []

        # def dfs(root, t, s):
        #     if t == root:
        #         if s == 0:
        #             p.append(root)
        #         else:
        #             q.append(root)
                
        #         return 0

            

            
            

        