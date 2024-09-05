class TrieNode:
    def __init__(self):
        self.children ={}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:
        def dfs(root, j):
            curr = root

            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.eow

        return dfs(self.root, 0) 


        # curr = self.root
        # searchWord = []

        # for c in word:
        #     if c in curr.children:
        #         searchWord.append(curr)
        #         curr = curr.children[c]
        #     elif c == '.':

        #     else:
        #         return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)