class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        L1 = len(nums1)
        L2 = len(nums2)
        
        dp = [[0] * (L2+1) for i in range(L1 + 1) ]

        
        for i in range(L1 - 1, -1, -1):
            for j in range(L2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                        
        return max(max(row) for row in dp)
                        
                    
                    
                    
                
        
