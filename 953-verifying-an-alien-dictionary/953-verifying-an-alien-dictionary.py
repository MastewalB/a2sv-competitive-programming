from functools import cmp_to_key

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        W = {}
        for i, v in enumerate(order):
            W[v] = i
        
        
        def comp(x, y):
            for i in range(min(len(x), len(y))):
                if W[x[i]] > W[y[i]]:
                    return 1
                elif W[x[i]] < W[y[i]]:
                    return -1
            if len(x) > len(y):
                return 1
            elif len(x) < len(y):
                return -1
            return 0
        
        
        words_sorted = sorted(words, key = cmp_to_key(comp))
        
        return words_sorted == words