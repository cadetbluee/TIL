from collections import deque
import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
land=[[5]*N for _ in range(N)]
A=[list(map(int,input().split())) for _ in range(N)]
trees=deque()
for _ in range(M):
    r, c, height = map(int, input().split())
    trees.append([r-1,c-1,height])

dirs=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
for _ in range(K):
   
    tree_len=len(trees)
    fertile=[]
    temp=[]
    for _ in range(tree_len):
        i,j,height=trees.popleft()
        if land[i][j]>=height:
            land[i][j]-=height
            trees.append([i,j,height+1])
            temp.append([i,j,height+1])
        else:
            fertile.append([i,j,height])
    for i,j,height in fertile:
        land[i][j]+=height//2
    for i,j,height in temp:
      
        
        if height%5==0:
            for d in dirs:
                ni=i+d[0]
                nj=j+d[1]
                if 0<=ni<N and 0<=nj<N:
                    trees.appendleft([ni,nj,1])
    for r in range(N):
        for c in range(N):
            land[r][c]+=A[r][c]
print(len(trees))    