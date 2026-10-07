class Solution:
    def numSquares(self, n: int) -> int:
        while n%4 == 0:
            n//=4
        
        if n%8 == 7: #n congruent to 7 mod 8
            return 4
        
        def isPerfSquare(num):
            s = int(math.sqrt(num))
            return s*s==num
        
        if isPerfSquare(n): return 1
        i = 1
        while i*i<=n:
            if isPerfSquare(n-i*i):
                return 2
            i+=1
        
        return 3