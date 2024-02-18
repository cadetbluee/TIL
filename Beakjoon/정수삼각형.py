n=int(input())
dp=[[] for _ in range(n)]
dp[0].append(int(input()))
for i in range(1,n):
    lis=list(map(int,input().split()))
    dp[i].append(dp[i-1][0]+lis[0])
    for j in range(1,i):
        dp[i].append(max(dp[i-1][j-1]+lis[j],dp[i-1][j]+lis[j]))
    dp[i].append(dp[i-1][i-1]+lis[i])
print(max(dp[n-1]))