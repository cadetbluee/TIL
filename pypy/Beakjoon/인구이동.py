import sys
sys.stdin=open('16234_input.txt')

from collections import deque
N,L,R=map(int,input().split())
population=list(list(map(int,input().split())) for _ in range(N))
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
answer=0
while True:
    visited=[[False]*N for _ in range(N)]
    moved=False
    changes = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j]=True
                union=[(i,j)]
                total=population[i][j]
                q=deque()
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                            gap=abs(population[i][j]-population[nx][ny])
                            if L<=gap<=R:
                                visited[nx][ny]=True
                                q.append((nx,ny))
                                union.append((nx,ny))
                                total+=population[nx][ny]
                if len(union)>1:
                    moved=True
                    n_pop=total//len(union)
                    changes.append((union,n_pop))
                    # for x,y in union:
                    #     population[x][y]=n_pop
                    # moved=True
    for union, n_pop in changes:
        for r,c in union:
            population[r][c] = n_pop
    if moved==False:
        break
    answer+=1
print(answer)
