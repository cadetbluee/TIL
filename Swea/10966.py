import sys
sys.stdin=open('10966_input.txt')
from collections import deque
dirs=[(0,1),(1,0),(0,-1),(-1,0)]

# def min_water(i,j,cnt):
#     global min_cnt
#     if arr[i][j]=='W':
#         if cnt<min_cnt:
#             min_cnt=cnt
#         return
#     elif cnt>min_cnt:
#         return
#     for d in dirs:
#         ni=d[0]+i
#         nj=d[1]+j
#         if 0<=ni<N and 0<=nj<M:
#             min_water(ni,nj,cnt+1)


T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[input().strip()for _ in range(N)]
    visited=[[-1]*M for _ in range(N)]
    ans=0
    Q=deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='W':
                visited[i][j]=0
                Q.append((i,j))
    while Q:
        i,j=Q.popleft()
        for d in dirs:
            ni=d[0]+i
            nj=d[1]+j
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==-1:
                visited[ni][nj]=visited[i][j]+1
                Q.append((ni,nj))
    for i in range(N):
        ans+=sum(visited[i])

    print(f'#{tc} {ans}')