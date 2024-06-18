import sys
sys.stdin = open("12712_input.txt", "r")
dirs1=[(1,0),(0,1),(-1,0),(0,-1)]
dirs2=[(1,1),(-1,-1),(-1,1),(1,-1)]
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_sum=0
    for i in range(N):
        for j in range(N):
            sum_arr=arr[i][j]
            for d in dirs1:
                for m in range(1,M):
                    ni=i+d[0]*m
                    nj=j+d[1]*m
                    if 0<=ni<N and 0<=nj<N:
                        sum_arr+=arr[ni][nj]
            if max_sum<sum_arr:
                max_sum=sum_arr
    for i in range(N):
        for j in range(N):
            sum_arr=arr[i][j]
            for d in dirs2:
                for m in range(1,M):
                    ni=i+d[0]*m
                    nj=j+d[1]*m
                    if 0<=ni<N and 0<=nj<N:
                        sum_arr+=arr[ni][nj]
            if max_sum<sum_arr:
                max_sum=sum_arr
    print(f'#{tc} {max_sum}')