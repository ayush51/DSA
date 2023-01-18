class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()

        n = len(nums1)

        if n % 2 != 0:
            return nums1[n//2]
        else:
            return (nums1[n//2] + nums1[n//2 - 1])/2
        
        
        
        ###################################################
        
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        last = m + n - 1

        for i in range(n):
            nums1.append(0)

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n-1]
            n,last = n-1,last-1

        length = len(nums1)

        if length % 2 != 0:
            return nums1[length//2]
        else:
            return (nums1[length//2] + nums1[length//2 - 1])/2
        
