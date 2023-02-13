class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = ("0" * (len(a) - len(b))) + b
        else:
            a = ("0" * (len(b) - len(a))) + a
        
        output = ""
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            res = int(a[i]) + int(b[i]) + carry
            if res == 3:
                output += "1"
                carry = 1
            elif res == 2:
                output += "0"
                carry = 1
            else:
                output += str(res)
                carry = 0
        if carry > 0:
            output += str(carry)
        return output[::-1]