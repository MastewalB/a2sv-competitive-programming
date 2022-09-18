class Trie:
    def __init__(self):
        CHAR_SIZE = 26
        self.isLeaf = False
        self.visited = 0
        self.index = []
        self.children = [None] * CHAR_SIZE
        
    def insert(self, word, pos):
        curr = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Trie()
            curr = curr.children[index]
            curr.visited += 1
        curr.isLeaf = True 
        curr.index.append(pos)
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        res = [None] * len(words)
        
        for i in range(len(words)):
            trie.insert(words[i], i)
        
        for i in range(len(words)):
            if not res[i]:
                word = words[i]
                curr = trie
                total = 0
                for j in range(len(word)):
                    index = ord(word[j]) - ord('a')
                    curr = curr.children[index]
                    total += curr.visited
                    if curr.isLeaf:
                        for k in curr.index:
                            res[k] = total
        
        return res