class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        self.nums = nums
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

S = Solution()
S.removeDuplicates([1,1,2])