import sys
input=sys.stdin.readline
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
idx=[0]*N
visited=[0]*(N)
min_gap=1e9
def recur(i,idx):
    global min_gap
    if i==N//2:
        
        sum_1=0
        sum_2=0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    sum_1+=arr[i][j]
                elif not visited[i] and not visited[j]:
                    sum_2+=arr[i][j]

        min_gap=min(min_gap,abs(sum_2-sum_1))
        
        return
    for j in range(idx,N):
        if visited[j]:
            continue
        visited[j]=1
        recur(i+1,j+1)
        visited[j]=0
        
recur(0,0)
print(min_gap)