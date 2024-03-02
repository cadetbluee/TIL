import sys
sys.stdin=open('1953_input.txt')
from collections import deque
dirs=[[(1,0),(0,1),(-1,0),(0,-1)],[(1,0),(-1,0)],[(0,1),(0,-1)],[(-1,0),(0,1)],[(1,0),(0,1)],[(1,0),(0,-1)],[(-1,0),(0,-1)]]
T=int(input())
for tc in range(1,T+1):
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[0]*M for _ in range(N)]
    Q=deque()
    Q.append((R,C))

    cnt=1
    while cnt<L:
        cnt+=1
        new_Q=[]
        while Q:
            i,j=Q.popleft()
            for d in dirs[arr[i][j]-1]:
                ni=d[0]+i
                nj=d[1]+j
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=0:
                    visited[ni][nj]=1
                    new_Q.append((ni,nj))
        Q.extend(new_Q)
    ans=0
    for i in range(N):
        ans+=sum(visited[i])
    print(ans)