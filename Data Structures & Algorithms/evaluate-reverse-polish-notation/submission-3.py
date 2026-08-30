class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2//n1)
            else:
                stack.append(int(token))
        return stack.pop()