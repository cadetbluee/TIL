N=int(input())
dp=[[0]*10 for _ in range(N+1)]
if len(dp)>0:
    dp[1][0]=0
    for i in range(1,10):
        dp[1][i]=1
if len(dp)>1:
    for i in range(2,N):
        dp[i][0]=dp[i]
        for j in range(10):
            dp[i][j]=dp[i-1][j]*2-2+dp[i-2]
print(dp[N-1]%1000000000)