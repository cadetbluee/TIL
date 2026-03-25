import sys
sys.stdin=open('21608_input.txt')

N=int(input())
board=[[0]*N for _ in range(N)]
# print(board)
like=dict()
for _ in range(N**2):
    s,p1,p2,p3,p4=map(int,input().split())
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸
    # 1을 만족하는 칸이 여러개면 인접한 칸 비어있는 칸 많은 곳
    # 2를 만족하는 칸 여러개면 행의 번호 가장 작고 열의 번호 가장 작은 곳
    like[s]=set({p1,p2,p3,p4})
    cands=[]
    for r in range(N):
        for c in range(N):
            if board[r][c]!=0:
                continue
            fav=0
            empty=0
            for d in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr=r+d[0]
                nc=c+d[1]
                if 0<=nr<N and 0<=nc<N:
                    if board[nr][nc] in like[s]:
                        fav+=1
                    elif board[nr][nc]==0:
                        empty+=1
            cands.append((-fav,-empty,r,c))
    cands.sort()
    # print(cands)
    r,c=cands[0][2],cands[0][3]
    board[r][c]=s

# print(board)
answer=0
for r in range(N):
    for c in range(N):
        fav=0
        s=board[r][c]
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr=r+d[0]
            nc=c+d[1]
            if 0<=nr<N and 0<=nc<N:
                if board[nr][nc] in like[s]:
                    fav+=1
        if fav>0:
            answer+=10**(fav-1)
print(answer)