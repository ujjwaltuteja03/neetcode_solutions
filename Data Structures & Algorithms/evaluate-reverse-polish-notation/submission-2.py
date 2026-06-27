class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for entry in tokens:
            if entry not in "+-/*": 
                stack.append(int(entry))
                continue
            elif entry == "+":
                stack.append(stack.pop()+stack.pop())
            elif entry == "-":
                second=stack.pop()
                first=stack.pop()
                stack.append(first-second)
            elif entry == "*":
                stack.append(stack.pop()*stack.pop())
            elif entry == "/":
                second=stack.pop()
                first=stack.pop()
                stack.append(int(first/second))
        return stack.pop()