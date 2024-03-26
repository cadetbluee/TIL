T=int(input())
for _ in range(T):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(2)]
    dp=[0]*N
    dp[0]=max(arr[0][0],arr[0][1])
    if N>1: dp[1]=max(arr[0][0]+arr[1][1],arr[0][1]+arr[1][0])
    