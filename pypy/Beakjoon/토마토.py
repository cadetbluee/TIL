import sys
sys.stdin=open('7576_input.txt')
from collections import deque
M,N=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(N)]
tomatoes=deque([(i,j) for i in range(N) for j in range(M) if box[i][j]==1])
dirs=[(1,0),(0,1),(-1,0),(0,-1)]

while tomatoes:
    i,j=tomatoes.popleft()
    for d in dirs:
        ni=i+d[0]
        nj=j+d[1]
        if 0<=ni<N and 0<=nj<M and box[ni][nj]==0:
            box[ni][nj]=box[i][j]+1
            tomatoes.append((ni,nj))
answer=0
for tomato in box:
    for i in tomato:
        if i==0:
            print(-1)
            sys.exit(0)
        elif answer<i:
            answer=i
print(answer-1)
        