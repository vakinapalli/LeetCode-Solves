class WordDictionary:

    class Node:
        def __init__(self):
            self.children = dict()
            self.word = False


    def __init__(self):
        self.root = self.Node()
        

    def addWord(self, word: str) -> None:
        hold = self.root
        for i in word:
            if i not in hold.children:
                hold.children[i] = self.Node()
            hold = hold.children[i]
        hold.word = True
    

        
    def recur(self,node, word, i):
        if i == len(word):
            return node.word
        if word[i] == '.':

            a = False
            for j in node.children:
                a = a | self.recur(node.children[j], word, i+1)
            return a
        elif word[i] in node.children:
        
            return self.recur(node.children[word[i]], word, i+1)
        else:
            return False
            
    def search(self, word: str) -> bool:
        return self.recur(self.root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)