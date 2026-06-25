class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for c in s:
            if c =='[' or c =='{' or c =='(': stack.append(c)
            else:
                if len(stack)==0:
                    return False
            
                top = stack[-1]
                if top != pairs[c]:
                    return False
                stack.pop()
        return len(stack)==0