N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1,N+1):
    graph[i]=sorted(graph[i],reverse=True)
visited=[0]*(N+1)
path=[]
def dfs(start):
    stack=[start]
    while stack:
        now=stack.pop()
        if visited[now]:
            continue
        path.append(now)
        visited[now]=1
        for to in graph[now]:
            stack.append(to)
dfs(V)
print(*path)
visited=[0]*(N+1)
path=[]
for i in range(1,N+1):
    graph[i]=sorted(graph[i])
def bfs(start):
    queue=[start]
    while queue:
        now=queue.pop(0)
        if visited[now]:
            continue
        path.append(now)
        visited[now]=1
        for to in graph[now]:
            queue.append(to)
bfs(V)
print(*path)