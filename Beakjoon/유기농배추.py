T=int(input())

def bfs(start):
    global cnt
    cnt+=1
    stack=[start]
    while stack:
        i,j=stack.pop()
        arr[i][j]=0
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni=i+d[0]
            nj=j+d[1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]:
                stack.append((ni,nj))

for _ in range(T):
    M,N,K=map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y=map(int,input().split())
        arr[Y][X]=1
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                bfs((i,j))
    print(cnt)
