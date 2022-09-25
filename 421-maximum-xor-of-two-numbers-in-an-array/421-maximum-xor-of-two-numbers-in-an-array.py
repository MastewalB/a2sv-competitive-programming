class Trie:
    def __init__(self):
        self.children = [None, None]
        
    
    def insert(self, number):
        curr = self
        for i in range(31, -1, -1):
            val = (number >> i) & 1
            if curr.children[val] == None:
                curr.children[val] = Trie()
            curr = curr.children[val]
    
    def search(self, number):
        curr = self
        result = 0
        
        for i in range(31, -1, -1):
            val = (number >> i) & 1
            if curr.children[1 - val] != None:
                result |= (1 << i)
                curr = curr.children[1 - val]
            else:
                curr = curr.children[val]
        
        return result
            
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        result = 0
        for num in nums:
            trie.insert(num)
        
        for num in nums:
            result = max(result, trie.search(num))
        
        return result
