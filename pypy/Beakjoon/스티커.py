T=int(input())
for _ in range(T):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(2)]
    dp=[[0]*N for _ in range(2)]
    dp[0][0]=arr[0][0]
    dp[1][0]=max(arr[0][0],arr[1][0])
    if N>1: 
        dp[0][1]=max(arr[0][0],arr[0][1]+arr[1][0])
        dp[1][1]=max(arr[0][0]+arr[1][1],arr[0][1]+arr[1][0])
    for i in range(2,N):
        dp[0][i]=max(dp[1][i-2]+arr[0][i],dp[0][i-2]+arr[1][i-1]+arr[0][i],dp[1][i-1])
        dp[1][i]=max(dp[0][i-1]+arr[1][i],dp[1][i-2]+arr[1][i],dp[0][i])
    print(dp[1][N-1])