import sys
sys.stdin = open('2105_input.txt')

def move(d,i,j,cnt):
    ni=i+dirs[d][0]
    nj=j+dirs[d][1]
    if 0<=ni<N and 0<=nj<N and visited[arr[i][j]]==0:
        visited[arr[i][j]]=1
        dessert(d,ni,nj,cnt+1,1)
        visited[arr[i][j]]=0
        
def dessert(d,i,j,cnt,switch):
    global max_cnt
    if d==3 and i==y:
        max_cnt=max(cnt,max_cnt)
        return
    if d==2 and i+j==y+x:
        dessert(d+1,i,j,cnt,0)
    move(d,i,j,cnt)
    if switch and d<2:
        dessert(d+1,i,j,cnt,0)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dirs=[(-1,-1),(-1,1),(1,1),(1,-1)]
    visited=[0]*101
    max_cnt=-1
    for y in range(N):
        for x in range(N):
            dessert(0,y,x,0,0)
    print(f'#{tc}',max_cnt)