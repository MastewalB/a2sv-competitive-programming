class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k <= 2:
            return k - 1
        mirror = 2 ** (n-1)

        if k <= mirror / 2:
            return self.kthGrammar(n - 1, k)
        else:
            return self.invert(self.kthGrammar(n - 1, k - mirror // 2))

    def invert(self, bit):
        return 1 - bit
