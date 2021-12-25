class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        stack = []
        space = 0
        total_space = 0
        stack_max = height[0]

        for i in range(1, len(height)):
            if height[i] > stack_max:

                for j in range(len(stack)):
                    value = stack.pop()
                    space += (height[i] - value) - (height[i] - stack_max)

                total_space += space
                space = 0
                stack_max = height[i]

            elif height[i] == stack_max:

                for j in range(len(stack)):
                    value = stack.pop()
                    space += (height[i] - value)

                total_space += space
                space = 0
                stack_max = height[i]

            else:
                stack.append(height[i])
        if len(stack) > 0:

            stack_max = stack.pop()
            for i in range(len(stack)):
                value = stack.pop()

                if value < stack_max:
                    space += stack_max - value
                    total_space += space
                    space = 0

                elif value == stack_max:

                    space = 0
                    stack_max = value

                else:

                    space = 0
                    stack_max = value

        return total_space
