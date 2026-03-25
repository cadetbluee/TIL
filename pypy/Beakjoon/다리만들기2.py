import sys
from pprint import pprint
sys.stdin=open('2146_input.txt')
N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]
pprint(board)
bridge=[]
dirs=[(1,0),(0,1),(0,-1),(-1,0)]
visited=[[0]*N for _ in range(N)]
stack=[(0,0)]
island=1
while stack:
    i,j=stack.pop()
    for di,dj in dirs:
        ni=i+di
        nj=j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
            visited[ni][nj]=1
            stack.append((ni,nj))
            if board[ni][nj]==1:
                board[ni][nj]=island
            elif board[ni][nj]==0:
                island+=1
    

for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            for di,dj in dirs:
                ni=i+di
                nj=j+dj
                if 0<=ni<N and 0<=nj<N and board[ni][nj]==0:
                    bridge.append((i,j,board[i][j]))