import sys
# import pprint
sys.stdin=open("3190_input.txt")
from collections import deque

N=int(input())
board=[[0]*N for _ in range(N)] # N*N판

K=int(input())

for _ in range(K):
    i,j=map(int,input().split())
    board[i-1][j-1]=2 #사과 표시

L=int(input())
cnt=0 #시간
snake=deque()
snake.append([0,0])
board[0][0]=1
direction=[(0,1),(1,0),(0,-1),(-1,0)] #오른쪽,아래,왼쪽,위
d=0 #현재 방향(오른쪽)
turn=dict()
for _ in range(L):
    X,C=input().split()
    turn[int(X)]=C

while True:
    cnt+=1
    i,j=snake[-1]
    
    ni=i+direction[d][0]
    nj=j+direction[d][1]
    
    if not (0<=ni<N and 0<=nj<N) or board[ni][nj]==1:
        print(cnt)
        break
    if board[ni][nj]==2:
        board[ni][nj]=1
        snake.append([ni,nj])
    else:
        board[ni][nj]=1
        ti,tj=snake.popleft()
        board[ti][tj]=0
        snake.append([ni,nj])
    if cnt in turn:
        if turn[cnt] == 'D':      # 오른쪽 회전(시계방향)
            d = (d + 1) % 4
        elif turn[cnt] == 'L':    # 왼쪽 회전(반시계)
            d = (d - 1) % 4