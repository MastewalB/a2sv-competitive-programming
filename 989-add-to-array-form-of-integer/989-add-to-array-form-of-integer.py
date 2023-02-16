class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        i = len(num) - 1
        while k > 0 and i >= 0:
            res = num[i] + (k % 10) + carry
            carry = 0
            if res > 9:
                carry = res // 10
                res %= 10
            result.append(res)
            k //= 10
            i -= 1
        if k > 0:
            while k > 0:
                res = (k % 10) + carry
                carry = 0
                if res > 9:
                    carry = res // 10
                    res %= 10
                result.append(res)
                k //= 10
        if i >= 0:
            while i >= 0:
                res = num[i] + carry
                carry = 0
                if res > 9:
                    carry = res // 10
                    res %= 10
                result.append(res)
                i -= 1
        if carry > 0:
            result.append(carry)
        return reversed(result)