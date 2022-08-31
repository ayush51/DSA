class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0;
        for i in range(0, len(nums)):
            counter = 0;
            while nums[i]!=0:
                nums[i]=nums[i]//10;
                counter +=1;
            if counter%2 == 0:
                result +=1;
        return result;


def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            s = str(num)
            if len(s) % 2 == 0:
                count += 1
        return count
        
