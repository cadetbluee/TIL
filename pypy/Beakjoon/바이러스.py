N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
visited=[0]*(N+1)
def dfs(start):
    stack=[start]
    while stack:
        now=stack.pop()
        if visited[now]:
            continue
        visited[now]=1
        for to in graph[now]:
            stack.append(to)
dfs(1)
print(visited.count(1)-1)