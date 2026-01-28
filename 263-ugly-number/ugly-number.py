class Solution:
    def isUgly(self, n: int) -> bool:
        if n<= 0:
            return False
        
        for Factors in [2,3,5]:
            while n % Factors == 0:
                n //= Factors

        return n == 1