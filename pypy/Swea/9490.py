import sys
sys.stdin = open("9490_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    # dirs=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
    max_m=0
    def dirs(M):
        results=[]
        for i in range(1,M+1):
            results.extend([(0,i),(0,-i),(i,0),(-i,0)])
        return results
    for i in range(N):
        for j in range(M):
            sum_m=arr[i][j]
            for d in dirs(arr[i][j]):
                ni=i+d[0]
                nj=j+d[1]
                if 0<=ni<N and 0<=nj<M:
                    sum_m+=arr[ni][nj]

            if max_m<sum_m:
                max_m=sum_m
    print(max_m)