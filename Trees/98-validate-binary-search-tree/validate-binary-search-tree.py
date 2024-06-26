# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(n, l, r):
            if not n:
                return True

            if not (n.val > l and n.val < r):
                return False

            return valid(n.left, l, n.val) and valid(n.right, n.val, r)

        return valid(root, float("-inf"), float("inf"))

        # def dfs(root, prevNode, lboundary, rboundary):
        #     if not root:
        #         return True
            
        #     valid = True
        #     if prevNode.left == root:
        #         if prevNode.val > root.val and root.val < treeMax:
        #             valid = True
        #         else:
        #             valid = False
        #     else:
        #         if prevNode.val < root.val and root.val > treeMax:
        #             valid = True
        #         else:
        #             valid = False
            
        #     if not valid:
        #         return False

        #     treeMax = max(treeMax, root.val)

        #     return dfs(root.left, root, treeMax) and dfs(root.right, root, treeMax)

        # return dfs(root.left, root, root.val, root.val) and dfs(root.right, root, root.val, root.val)

        