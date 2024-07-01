# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        q = deque([root])

        while q:
            lenq = len(q)
            for i in range(lenq):
                n = q.popleft()
                if n:
                    res += str(n.val)+" "
                    l = n.left
                    r = n.right
                    q.append(l)
                    q.append(r)
                else:
                    res += 'n '

        return str(res)

                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

        if data[0] == 'n':
            return None

        data = data.split()
        
        root = TreeNode(int(data[0]))
        curr = root
        q = deque([root])
        i = 1
        while q and i< len(data):
            n = q.popleft()
            if data[i] != 'n':
                left = TreeNode(int(data[i]))
                n.left = left
                q.append(left)
            i+=1
            if data[i] != 'n':
                right = TreeNode(int(data[i]))
                n.right = right
                q.append(right)
            i+=1
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))