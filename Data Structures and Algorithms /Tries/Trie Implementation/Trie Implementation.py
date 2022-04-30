class Trie:

    def __init__(self):
        CHAR_SIZE = 26
        self.isLeaf = False
        self.children = [None] * CHAR_SIZE

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Trie()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
