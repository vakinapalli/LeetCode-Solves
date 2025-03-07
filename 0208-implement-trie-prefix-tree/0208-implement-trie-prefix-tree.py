class Trie:

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.kids:
                cur.kids[i] = self.Node()
            cur = cur.kids[i]
        cur.word = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.kids:
                return False
            cur = cur.kids[i]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.kids:
                return False
            cur = cur.kids[i]
        return True

    
    class Node:
        def __init__(self):
            self.kids = dict()
            self.word = False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)