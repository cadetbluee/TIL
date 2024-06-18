import sys
sys.stdin=open("1149_input.txt")
N=int(input())
dp=[[0]*3 for _ in range(N)] 
dp[0][0],dp[0][1],dp[0][2]=map(int,input().split())

for i in range(1,N):
    r,g,b=map(int,input().split())
    dp[i][0],dp[i][1],dp[i][2]=min(dp[i-1][1]+r,dp[i-1][2]+r),min(dp[i-1][0]+g,dp[i-1][2]+g),min(dp[i-1][0]+b,dp[i-1][1]+b)
print(min(dp[N-1]))
