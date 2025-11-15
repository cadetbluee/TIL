import sys
import pprint
sys.stdin=open("14502_input.txt")
# from copy import deepcopy
from collections import deque


N,M=map(int,input().split())
lab=[list(map(int,input().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
virus=[(i,j) for i in range(N) for j in range(M) if lab[i][j]==2]
empties=[(i,j) for i in range(N) for j in range(M) if lab[i][j]==0]
Z=len(empties)

def spread():
    dir=[(1,0),(-1,0),(0,1),(0,-1)]
   
    # N,M=len(lab),len(lab[0])
    spreadedLab=[row[:] for row in lab]
    q=deque(virus)
    safe=Z-3
    while q:
        # pprint.pprint(lab)
        # pprint.pprint(virus)
        i,j=q.popleft()
        if spreadedLab[i][j]==2:
            for d in dir:
                ni=i+d[0]
                nj=j+d[1]
                if (0<=ni<N and 0<=nj<M) and spreadedLab[ni][nj]==0:
                    spreadedLab[ni][nj]=2
                    safe-=1
                    # if 
                    q.append([ni,nj])
    return safe
# def countSafeSpace(lab):
#     N,M=len(lab),len(lab[0])
#     cnt=0
#     for i in range(N):
#         for j in range(M):
#             if lab[i][j]==0:
#                 cnt+=1
#     return cnt
maxS=0
def patition(level,start):
    global maxS
    if level==3:
        # pprint.pprint(lab)
        safeSpace=spread()
        if safeSpace>maxS:
            maxS=safeSpace
        return
    for k in range(start,Z):
        i,j=empties[k]
        if lab[i][j]==0:
            lab[i][j]=1
            patition(level+1,start+1)
            lab[i][j]=0
patition(0,0)
print(maxS)