import sys
sys.stdin = open("1220_input.txt", "r")
T=10
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    prei=N
    cnt=0
    for j in range(N):
        for i in range(N):
            if arr[i][j]==1:
                prei=i
            elif arr[i][j]==2 and i>prei:
                cnt+=1
                prei=N
    print(f'#{tc} {cnt}')