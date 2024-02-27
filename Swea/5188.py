import sys
sys.stdin=open('5188_input.txt')
dirs=[(0,1),(1,0)]


def min_sum(i,j,N,s):
    global min_s
    if i==N-1 and j==N-1:
        if min_s>s+arr[i][j]:
            min_s=s+arr[i][j]
        return
    elif s>min_s:
        return
    for d in dirs:
        if 0<=i+d[0]<N and 0<=j+d[1]<N:
            min_sum(i+d[0],j+d[1],N,s+arr[i][j])


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_s=1e9
    min_sum(0,0,N,0)
    print(f'#{tc} {min_s}')
