class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]


sl = Solution().twoSum([2, 7, 11, 15], 9)
print(sl)