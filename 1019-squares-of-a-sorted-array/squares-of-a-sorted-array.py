class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        self.nums = nums
        res = []
        for x in nums:
            res.append(x * x)
        res.sort()
        return res