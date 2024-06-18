def dfs(start,end):
    stack=[start]

    cnt=0
    while stack:
        now=stack.pop()
        if cnt>0 and now==end:
            return 1
        if visited[now]:
            continue
        visited[now]=1
        for to in graph[now]:
            stack.append(to)
        cnt+=1
    return 0
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
graph=[[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            graph[i].append(j)
            # graph[j].append(i)
ans=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        start,end=i,j
        visited=[0]*N
        ans[i][j]=dfs(start,end)
for a in ans:
    print(*a)