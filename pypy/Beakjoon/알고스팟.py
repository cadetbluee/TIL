import sys
from collections import deque
sys.stdin=open('1261_input.txt')
M,N=map(int,input().split())
minC=N*M
board=[list(map(int, input().strip())) for _ in range(N)]
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
stack=[(0,0)]


dist = [[10**9]*M for _ in range(N)]
dist[0][0]=0

dq=deque()
dq.append((0,0))

while dq:
    i,j=dq.popleft()
    for di,dj in dirs:
        ni,nj=i+di,j+dj
        if 0<=ni<N and 0<=nj<M:
            weight=board[ni][nj]
            nd = dist[i][j] + weight
            if nd<dist[ni][nj]:
                dist[ni][nj]=nd
                if weight==0:
                    dq.appendleft((ni,nj))
                else:
                    dq.append((ni,nj))
print(dist[N-1][M-1])