def isValid(self, s):
    char_stack = []

    for i in s:
        if i in "( { [":
            char_stack.append(i)
        else:
            if len(char_stack) == 0:
                return False

            elif i == ")":

                if char_stack.pop() != "(":
                    return False
            elif i == "}":

                if char_stack.pop() != "{":
                    return False
            elif i == "]":

                if char_stack.pop() != "[":
                    return False
            else:
                return False
    if len(char_stack) == 0:
        return True
    return False
