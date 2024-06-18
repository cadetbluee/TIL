import sys
sys.stdin = open('1865_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    idx=[0 for i in range(N)]
    visited=[]
    max_per=0
    def project(i,s):
        global max_per
        if i==N:
            max_per=max(max_per,s*100)
            return
        elif s*100<=max_per:
            return
        for j in range(N):
            if j not in idx[:i]:
                idx[i]=j
                project(i+1,s*arr[i][idx[i]]*0.01)

    project(0,1)
    print(f'#{tc} {max_per:.6f}')