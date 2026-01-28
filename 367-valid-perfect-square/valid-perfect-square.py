class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 1, num // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= num:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans * ans == num

