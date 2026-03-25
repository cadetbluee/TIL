import sys
from collections import deque
sys.stdin=open('7562_input.txt')

N=int(input())
dirs=[(-1,2),(-2,1),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
for _ in range(N):
    I=int(input())
    S=tuple(map(int,input().split()))
    E=tuple(map(int,input().split()))
    visited = [[False]*I for _ in range(I)]
    queue = deque()
    queue.append((S, 0))
    visited[S[0]][S[1]] = True
    
    while queue:
        x, time = queue.popleft()

        if x == E:
            print(time)
            break
        i,j=x
        for d in dirs:
            ni=i+d[0]
            nj=j+d[1]
            if 0 <= ni <I and 0<=nj<I and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append(((ni,nj), time+1))