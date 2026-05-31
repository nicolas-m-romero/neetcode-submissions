class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case '+':
                    x, y = stack.pop(), stack.pop()
                    stack.append(y + x)
                case '-':
                    x, y = stack.pop(), stack.pop()
                    stack.append(y - x)
                case '*':
                    x, y = stack.pop(), stack.pop()
                    stack.append(int(y * x))
                case '/':
                    x, y = stack.pop(), stack.pop()
                    stack.append(int(y / x))
                case _:
                    stack.append(int(t))

        return stack[0]