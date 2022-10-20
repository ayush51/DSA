

dp = [False] * (n+1)

dp[len(s)] = True

for i in range(len(s)):
    for word in wordDict:
        if (i + len(w)) <= len(s) and s[i: i + len(w)] = w:
            dp[i] = dp[i + len(w)] 
            if dp[i]:
                break
return dp[0]                
