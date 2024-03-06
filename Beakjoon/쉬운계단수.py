N=int(input())
dp=[0]*N
if len(dp)>0: dp[0]=9
if len(dp)>1: dp[1]=dp[0]+dp[0]-1
for i in range(2,N):
    dp[i]=dp[i-1]+dp[i-1]-2
print(dp[N-1]%1000000000)
