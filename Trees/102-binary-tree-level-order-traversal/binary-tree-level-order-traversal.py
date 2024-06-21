# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root:
            return []
        q = deque()
        q.append(root)
        while q:
            qlen = len(q)
            lvl = []
            for i in range(qlen):
                e = q.popleft()
                if e:
                    lvl.append(e.val)
                    if e.left:
                        q.append(e.left)
                    if e.right:
                        q.append(e.right)

            res.append(lvl)


        return res
        