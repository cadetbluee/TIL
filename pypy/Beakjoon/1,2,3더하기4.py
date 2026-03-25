import sys
sys.stdin=open('15989_input.txt')
T=int(input())
n_list=[]
for _ in range(T):
    n=int(input())
    n_list.append(n)
max_n=max(n_list)
dp=[[0]*3 for _ in range(max_n)]
dp[0][0],dp[0][1],dp[0][2]=1,0,0
dp[1][0],dp[1][1],dp[1][2]=1,1,0
dp[2][0],dp[2][1],dp[2][2]=1,1,1
dp[3][0],dp[3][1],dp[3][2]=1,2,1
for i in range(4,max_n):
    dp[i][0]=1
    dp[i][1]=dp[i-2][0]+dp[i-2][1]
    dp[i][2]=dp[i-3][0]+dp[i-3][1]+dp[i-3][2]
for n in n_list:
    print(sum(dp[n-1]))