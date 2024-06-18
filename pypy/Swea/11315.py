import sys
sys.stdin = open("11315_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[input().strip() for _ in range(N)]
    result='NO'
    cnt=0
    for i in range(N):
        for j in range(N):
            if j+i<N and arr[j][j+i]=='o':
                cnt+=1
                if cnt>=5:
                    result = 'YES'
            else:
                cnt=0
    cnt
    for i in range(N):
        for j in range(N):
            if 0<=j+i<N and arr[j+i][j]=='o':
                cnt+=1
                if cnt>=5:
                    result = 'YES'
            else:
                cnt=0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if 0<=N-j-1+i <N and arr[j][N-j-1+i] == 'o':
                cnt += 1
                if cnt>=5:
                    result = 'YES'
            else:
                cnt=0
    cnt=0
    for i in range(N):
        for j in range(N):
            if 0<=j+i<N and arr[j+i][N-j-1] == 'o':
                cnt += 1
                if cnt>=5:
                    result = 'YES'
            else:
                cnt=0
    cnt=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='o':
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
            else:
                cnt = 0
    cnt=0
    for i in range(N):
        for j in range(N):
            if arr[j][i]=='o':
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
            else:
                cnt = 0

    print(f'#{tc} {result}')