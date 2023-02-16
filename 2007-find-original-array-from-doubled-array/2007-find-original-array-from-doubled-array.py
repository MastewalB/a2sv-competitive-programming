class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        count = Counter(changed)
        res = []
        
        for i in range(len(changed)):
            if count[changed[i]] > 0:
                res.append(changed[i])
                count[2 * changed[i]] -= 1
                count[changed[i]] -= 1
                if count[2 * changed[i]] == -1:
                    return []
                
        return res