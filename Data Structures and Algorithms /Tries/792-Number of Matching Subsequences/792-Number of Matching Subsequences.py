class Trie:
    def __init__(self):
        CHAR_SIZE = 26
        self.isLeaf = False
        self.children = [None] * CHAR_SIZE
        self.index = None

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Trie()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, word: str, s: str) -> None:
        curr = self

        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.children[index].index == None:
                curr.children[index].index = -1
                ind = curr.index + 1 if curr.index else 0
                for j in range(ind, len(s)):
                    if s[j] == word[i]:
                        curr.children[index].index = j
                        break
            if curr.children[index].index < 0:
                return False
            curr = curr.children[index]
        return True


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        words.sort()
        trie = Trie()
        count = 0

        for word in words:
            trie.insert(word)

        for word in words:
            count += trie.search(word, s)
        return count
