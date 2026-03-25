import sys
from pprint import pprint
from collections import deque
sys.stdin=open('19238_input.txt')
N,M,F=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
sr,sc=map(int,input().split())
customers=[list(map(int,input().split())) for _ in range(M)]

def bfs(start):
    visited=[[-1]*N for _ in range(N)]
    i,j=start
    visited[i][j]=0
    q=deque([(i,j,0)])
    
    while q:
        si,sj,dist=q.popleft()
        # if (si,sj)==end:
        #     return dist
        for d in [(1,0),(-1,0),(0,-1),(0,1)]:
            ni=si+d[0]
            nj=sj+d[1]
            if 0<=ni<N and 0<=nj<N and board[ni][nj]==0 and visited[ni][nj]==-1:
                visited[ni][nj]=dist+1
                q.append((ni,nj,dist+1))
    return visited

while customers:
    min_d=N*N+1
    t_idx=0
    # 1. 택시에서 손님
    n_board=bfs((sr-1,sc-1))
    for idx,customer in enumerate(customers):
        new_d=n_board[customer[0]-1][customer[1]-1]
        if new_d == -1:
            min_d=-1
            break
        if min_d>new_d:
            min_d=new_d
            t_idx=idx
        elif min_d==new_d and customers[t_idx][0]>customer[0]:
            min_d=new_d
            t_idx=idx
        elif min_d==new_d and customers[t_idx][0]==customer[0] and customers[t_idx][1]>customer[1]:
            min_d=new_d
            t_idx=idx
    selected=customers.pop(t_idx)
    F-=min_d
    if F<0 or min_d==-1:
        F=-1
        break
    # 2. 손님 옮기기
    f_c_board=bfs((selected[0]-1,selected[1]-1))
    f_c=f_c_board[selected[2]-1][selected[3]-1]
    if F<f_c or f_c==-1:
        F=-1
        break
    F+=f_c
    sr,sc=(selected[2],selected[3])
# bfs((sr-1,sc-1),(4,3))
print(F)
            