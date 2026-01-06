class Solution:
    def twoSum(self,num, target):
        self.num = num
        self.target = target
        for i in range(len(num)):
            for j in range (i+1, len(num)):
                res = []
                if num[i]+num[j]==target:
                    return [i,j]
            

S = Solution()
S.twoSum([2,7,11,15],9)