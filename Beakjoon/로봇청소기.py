N,M=map(int,input().split())
x,y,D=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
dirs=[(-1,0),(0,1),(1,0),(0,-1)]
stack=[(x,y,D)]
cnt=0
while stack:
    i,j,D=stack.pop()
    
    if arr[i][j]==0:
        cnt+=1
        arr[i][j]=-1
    switch=0
    for _ in range(4):
        D = (D+3) % 4
        ni=i+dirs[D][0]
        nj=j+dirs[D][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            stack.append((ni,nj,D))
            switch=1
            break
    if switch==0:
        if arr[i-dirs[D][0]][j-dirs[D][1]] == 1:
            print(cnt)
            break
        else:
            stack.append((i-dirs[D][0],j-dirs[D][1],D))
            