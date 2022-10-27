User1 = ["hi", "bye", "hello", "leetcode", "start", "end"]
User2 = ["hi", "stop", "leetcode", "start", "end", "bye"]
    
#User1 = ["hi", "bye", "hello"]
#User2 = ["leetcode", "start", "end"]
    
def longestRepeating(a,b):
    
    L1 = len(a)
    L2 = len(b)
    
    dp = [[0]*(L2+1) for _ in range(L1+1)]
    
    #print(dp)
    
    maxL = 0
    idx = 0
    for i in range(L1-1, -1, -1):
        for j in range(L2-1, -1, -1):
            print("i : {}, j : {}, a[i] : {}, b[j] : {}".format(i,j, a[i], b[j]))
            if a[i]==b[j]:
                print("dp[i][j] : {}, dp[i+1][j+1] : {}".format(dp[i][j], dp[i+1][j+1]))
                dp[i][j]=dp[i+1][j+1]+1
                print("dp[i][j] : {}, dp[i+1][j+1] : {}".format(dp[i][j], dp[i+1][j+1]))
                print("")
                if dp[i][j] > maxL:
                    idx = i
                    maxL = dp[i][j]
                    print("idx : {}, maxL : {}".format(idx, maxL))
    return a[idx:idx+maxL]

print(longestRepeating(User1, User2))
