class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""

        def decode(s):
            char = ""
            i = 0
            while i < len(s):
                if s[i] == "]":
                    if stack:
                        return (i, char)
                    result += char
                    char = ""
                elif s[i].isdigit():
                    digit = s[i]
                    for j in range(1, 3):
                        if s[i + j].isdigit():
                            digit += s[i + j]
                        else:
                            break
                    stack.append(digit)
                    i += len(digit) + 1
                    count, ch = decode(s[i:])
                    char += ch * int(stack.pop())
                    i += count
                else:
                    char += s[i]
                i += 1
            return char

        result += decode(s)
        return result
