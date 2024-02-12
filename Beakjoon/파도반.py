T=int(input())
for _ in range(T):
    N=int(input())
    dp=[0]*(N+1)
    dp[0],dp[1],dp[2]=1,1,1
    for i in range(2,N+1):
        dp[i]=dp[i-2]+dp[i-3]
    print(dp[N-1])