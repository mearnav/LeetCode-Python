class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s
        c = ""

        for ch in self.s:
            if ch.isalnum():
                c += ch.lower()
        return c == c[::-1]

S = Solution()
S.isPalindrome("A man, a plan, a canal: Panama")