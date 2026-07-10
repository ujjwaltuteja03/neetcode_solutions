class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open par if open<n
        # only add a closing par if closed<open
        # valid solution when open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        backtrack(0, 0)
        return res
