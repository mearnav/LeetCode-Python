class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        self.n = n
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3

        return n == 1

S = Solution()
S.isPowerOfThree(27)