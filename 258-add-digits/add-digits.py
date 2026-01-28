class Solution:
    def addDigits(self, num: int) -> int:
        seen = set()

        while num!= 1 and num not in seen:
            seen.add(num)

            total = 0
            while num>0:
                digits = num % 10
                total += digits
                num //= 10
            
            num = total

        return num