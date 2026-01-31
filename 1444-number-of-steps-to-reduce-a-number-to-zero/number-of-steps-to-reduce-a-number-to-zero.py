class Solution:
    def numberOfSteps(self, num: int) -> int:
        temp = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                 num -= 1
            temp += 1

        return temp   