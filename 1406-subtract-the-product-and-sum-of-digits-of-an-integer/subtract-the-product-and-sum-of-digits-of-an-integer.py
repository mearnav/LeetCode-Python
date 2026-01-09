class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        self.n = n
        temp = n
        sum_digit = 0
        prod_digit = 1

        while temp > 0:
            d = temp % 10
            prod_digit *= d 
            sum_digit += d
            temp //= 10
        return (prod_digit - sum_digit)