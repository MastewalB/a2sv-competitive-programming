class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        if k == 2 or k == 3:
            return "1"

        if math.ceil(math.log2(k)) == math.floor(math.log2(k)):
            return "1"

        threshold = pow(2, n)
        length = threshold - 1

        if k > threshold / 2:
            mirror = k - (2 * (k - (math.ceil(length / 2))))
            n -= 1
            return self.invert(self.findKthBit(n, mirror))
        else:
            n -= 1
            return self.findKthBit(n, k)

    def invert(self, bit):
        return "1" if bit == "0" else "0"
