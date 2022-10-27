class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        L1 = len(text1)
        L2 = len(text2)
        
        dp = [[0] * (L2+1) for r in range(L1 + 1)]
        
        for i in range(L1-1,-1,-1):     
            for j in range(L2 -1, -1, -1):    #iterating through end
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]   #since equal we go diagonal + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])  #since unequal we go max(right, down)
                    
        return dp[0][0]
