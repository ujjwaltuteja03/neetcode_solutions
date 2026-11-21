class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        one,two,three = 0,1,1
        i=3
        while i<=n:
            temp = three
            three = one+two+three
            one = two
            two = temp
            i+=1
        return three