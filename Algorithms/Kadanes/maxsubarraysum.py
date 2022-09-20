class Solution:
    def maxSubArraySum(self, nums: List[int]) -> int:
        sum = 0
        maxSum = -10000
        for i in range(len(nums)):
            sum += nums[i]
            maxSum = max(sum, maxSum)
            if sum<0:
                sum = 0
         return maxSum
