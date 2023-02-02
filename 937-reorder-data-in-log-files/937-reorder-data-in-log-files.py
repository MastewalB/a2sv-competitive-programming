class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                log = log.split(" ")
                log = tuple([log[1:], log[0]])
                letters.append(log)
        
        letters.sort()
        for i in range(len(letters)):
            letters[i] = letters[i][1] + ' ' + ' '.join(letters[i][0])
        
        return letters + digits