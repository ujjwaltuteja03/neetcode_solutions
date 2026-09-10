class Solution:
    def totalNQueens(self, n: int) -> int:
        col, pos, neg = set(), set(), set()
        res = 0

        def backtrack(r):
            nonlocal res
            if r==n:
                res+=1
                return
            
            for c in range(n):
                if c in col or r+c in pos or r-c in neg: continue

                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                
                backtrack(r+1)

                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        backtrack(0)
        return res