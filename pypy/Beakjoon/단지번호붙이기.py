def bfs(start):
    stack=[start]
    cnt=0
    while stack:
        i,j=stack.pop()
        if arr[i][j]: cnt+=1
        else:continue
        arr[i][j]=0
       
        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni=i+d[0]
            nj=j+d[1]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1:
                stack.append((ni,nj))
    return cnt
N=int(input())
arr=[list(map(int,input())) for _ in range(N)]
counts=[]

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            counts.append(bfs((i,j)))
print(len(counts))
for c in sorted(counts):
    print(c)