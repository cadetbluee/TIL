import copy
N,M=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(N)]
def check(arr):
    stack=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                stack.append((i,j))
    temp=copy.deepcopy(arr)
    while stack:
        i,j=stack.pop()
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni=i+d[0]
            nj=j+d[1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                temp[ni][nj]=2
                stack.append((ni,nj))
    cnt=0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                cnt+=1
                
    return cnt
possibilities=[]
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            possibilities.append((i,j))
visited=[0]*len(possibilities)
max_poss=0
def recur(i):
    global max_poss
    if i==3:
        max_poss=max(max_poss,check(arr))
        print(arr)
        return
    for idx,(r,c) in enumerate(possibilities):
        if arr[r][c]==0:
            arr[r][c]=1
            recur(i+1)
            arr[r][c]=0
    
recur(0)
print(max_poss)