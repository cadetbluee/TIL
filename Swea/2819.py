import sys
sys.stdin = open('2819_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    arr=[input().split() for _ in range(4)]
    dirs=[(1,0),(0,1),(-1,0),(0,-1)]
    ans=set()
    visited=[]
    def recur(i,j,a,n):
        if n==7:
            ans.add(a)
            return
        if a in ans:
            return

        for d in dirs:
            ni=d[0]+i
            nj=d[1]+j
            if 0<=ni<4 and 0<=nj<4:
                recur(ni,nj,a+arr[ni][nj],n+1)
    for i in range(4):
        for j in range(4):
            recur(i,j,'',0)
    print(f'#{tc}',len(ans))