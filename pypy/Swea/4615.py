import sys
sys.stdin = open("4615_input.txt", "r")

dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[[0]*N for _ in range(N)]
    arr[N//2][N//2]=2
    arr[N//2-1][N//2-1]=2
    arr[N // 2][N // 2-1] = 1
    arr[N // 2-1][N // 2] = 1

    for _ in range(M):
        j,i,color=map(int,input().split())
        for d in dirs:
            ni=i-1+d[0]
            nj=j-1+d[1]
            for k in range(2,N):
                ki=i-1+d[0]*k
                kj = j - 1 + d[1] * k
                if 0<=ni<N and 0<=nj<N and 0<=ki<N and 0<=kj<N:
                    if color==1 and arr[ni][nj]==2 and arr[ki][kj]==color:
                        for h in range(k+1):
                            arr[i-1+d[0]*h][j-1+d[1]*h]=color
                    elif color==2 and arr[ni][nj]==1 and arr[ki][kj]==color:
                        for h in range(k + 1):
                            arr[i - 1 + d[0] * h][j - 1 + d[1] * h] = color
                    elif arr[ki][kj]==0:
                        break

    cnt_black=0
    cnt_white=0

    for i in arr:
        for j in i:
            if j==1:
                cnt_black+=1
            elif j==2:
                cnt_white+=1
    print(f'#{tc} {cnt_black} {cnt_white}')