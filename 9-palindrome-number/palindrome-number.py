class Solution:
    def isPalindrome(self, x: int):
        self.x = x
        temp = self.x
        rev = 0
        while temp>0:
            d = temp % 10
            rev = rev * 10 + d
            temp //= 10
        return rev == self.x

S = Solution()
S.isPalindrome(121)