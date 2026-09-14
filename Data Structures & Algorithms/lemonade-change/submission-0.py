class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                if five>0:
                    five-=1
                else:
                    return False
            
            else:
                change = b-5
                if change == 15 and five>0 and ten>0:
                    five-=1
                    ten-=1
                elif change == 15 and five>=3:
                    five-=3
                elif change == 10 and ten>0:
                    ten-=1
                elif change == 10 and five>=2:
                    five-=2
                else: return False
        return True