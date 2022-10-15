class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        count = 0
        for i in range(2, len(nums)):
            l = 0
            r = i - 1
            while l<r:
                
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1

        return count
