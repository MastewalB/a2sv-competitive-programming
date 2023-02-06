class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        maxLength = 1
        chain = dict()
        
        words.sort(key=len)
        for word in words:
            chain[word] = 1
        
        for word in words:
            
            for i in range(len(word)):
                if chain.get(word[:i] + word[i+1:]):
                    chain[word] = max(chain[word], chain[word[:i] + word[i+1:]] + 1)
                    maxLength = max(maxLength, chain[word])
        
        return maxLength