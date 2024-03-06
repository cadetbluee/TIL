N=int(input())
stair=[]
for _ in range(N):
    stair.append(int(input()))
dp=[0]*N
if len(dp)>0:dp[0]=stair[0]
if len(dp)>1:dp[1]=stair[0]+stair[1]
if len(dp)>2:dp[2]=max(stair[0]+stair[2],stair[1]+stair[2])
for i in range(3,N):
    dp[i]=max(stair[i]+dp[i-2],stair[i]+stair[i-1]+dp[i-3])
print(dp[N-1])