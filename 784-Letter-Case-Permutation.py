class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        N = len(s)
        answer = [list(s)]

        for i in range(N):

            if s[i].isalpha():
                size = len(answer)
                for j in range(size):
                    curr = answer[j][:]
                    if curr[i].islower():
                        curr[i] = s[i].upper()
                        answer.append(curr[:])
                    else:
                        curr[i] = s[i].lower()
                        answer.append(curr)

        return list(map(lambda x: ''.join(x), answer))
