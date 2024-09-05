class Trie:
    def __init__(self):
        self.children = {}
        self.eow = False

    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.eow = True
    # def search(self, word):
    #     curr = self.root
    #     for c in word:
    #         if c not in curr.children:
    #             return False
    #         curr = curr.children[c]
    #     return cur.eow
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.add(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r,c,node,word):
            if (r < 0 or c<0 or c >= COLS or r >= ROWS or
            board[r][c] not in node.children or
            (r,c) in visited):
                return 

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.eow:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))
    
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)