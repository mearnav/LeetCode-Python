class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        self.h = haystack
        self.n = needle
        for i in range(len(self.h) - len(self.n) + 1):
            if self.h[i:i+len(self.n)] == self.n:
                return i
        return -1

S = Solution()
print(S.strStr("sadbutsad", "sad")) 