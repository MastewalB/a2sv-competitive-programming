class Trie:
    def __init__(self):
        CHAR_SIZE = 26
        self.isLeaf = False
        self.children = [None] * CHAR_SIZE 
    
    def searchPrefix(self, word: str) -> str:
        curr = self
        prefix = []
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            
            if curr.isLeaf:
                return ''.join(prefix)
            prefix.append(word[i])
            if not curr.children[index]:
                return ""
            
            curr = curr.children[index]
        
    
    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Trie()
            curr = curr.children[index]
        curr.isLeaf = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        sentence = sentence.split()
        for word in dictionary:
            trie.insert(word)
        
        for i in range(len(sentence)):
            prefix = trie.searchPrefix(sentence[i])
            if prefix:
                sentence[i] = prefix
        
        return ' '.join(sentence)
        