class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        self.nums = nums

        max_val = max(nums)
        idx = nums.index(max_val)

        for i in range(len(nums)):
            if nums[i] != max_val and max_val < 2 * nums[i]:
                return -1

        return idx