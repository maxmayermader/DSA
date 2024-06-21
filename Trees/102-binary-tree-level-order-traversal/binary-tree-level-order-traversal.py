# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root: #if empty 
            return []

        #start of BFS
        q = deque()
        q.append(root)
        while q:
            qlen = len(q) #how many items are in the Q
            lvl = [] 

            for i in range(qlen): #Run for the amount of items in Q. This is the level
                e = q.popleft()
                if e:  #if node is not null
                    lvl.append(e.val)
                    q.append(e.left)
                    q.append(e.right)
            if(lvl): #not empty
                res.append(lvl)


        return res
        


        # def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # res = []
        # q = collections.deque()
        # if root:
        #     q.append(root)

        # while q:
        #     val = []

        #     for i in range(len(q)):
        #         node = q.popleft()
        #         val.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(val)
        # return res