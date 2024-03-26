import sys
input=sys.stdin.readline
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
arr_sum=[[0]*(N+1) for _ in range(N+1)]
arr_sum[1][1]=arr[0][0]
for i in range(1,N):
    arr_sum[1][i+1]=arr[0][i]+arr_sum[1][i]
    arr_sum[i+1][1]=arr[i][0]+arr_sum[i][1]
for i in range(1,N):
    
    for j in range(1,N):
        arr_sum[i+1][j+1]=arr[i][j]+arr_sum[i+1][j]+arr_sum[i][j+1]-arr_sum[i][j]
for _ in range(M):
    x,y,i,j=map(int,input().split())
    print(arr_sum[i][j]+arr_sum[x-1][y-1]-arr_sum[x-1][j]-arr_sum[i][y-1])
