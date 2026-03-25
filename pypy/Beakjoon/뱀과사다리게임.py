import sys
sys.stdin=open('16928_input.txt')

from collections import deque

N,M=map(int,input().split())
move=dict()
# ladders=list(list(map(int,input().split()))for _ in range(N))
# snakes=list(list(map(int,input().split()))for _ in range(M))
for _ in range(N+M):
    x,y=map(int,input().split())
    move[x]=y
board=[0]*107
board[1]=1
que=deque()
que.append((1,0))
while que:
    cur,cnt=que.popleft()
    if cur==100:
        print(cnt)
        break
    elif cur>100:
        continue
    for i in range(1,7):
        next=cur+i
        
        if next in move:
            if board[move[next]]==0:
                board[move[next]]=1
                que.append((move[next],cnt+1))
        else:
            if board[next]==0:
                board[next]=1
                que.append((next,cnt+1))


