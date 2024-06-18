import sys
sys.stdin=open('1861_input.txt')
sys.setrecursionlimit(5000)
dirs=[(0,1),(1,0),(0,-1),(-1,0)]
def move_room(i,j):
    global cnt
    cnt+=1

    for d in dirs:
        ni=i+d[0]
        nj=j+d[1]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]==(arr[i][j]+1):

                move_room(ni,nj)



T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt=0
    visit=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0:
                cnt = 0
                visit[i][j] = 1
                move_room(i,j)
                visit[i][j] = 0
                if max_cnt<cnt:
                    max_cnt=cnt
                    max_i=arr[i][j]
                elif max_cnt==cnt:
                    max_i=min(arr[i][j],max_i)

    print(f'#{tc} {max_i} {max_cnt}')