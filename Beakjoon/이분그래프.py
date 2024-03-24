from collections import deque
K=int(input())
def bfs(start):
    Q=deque()
    Q.append(start)
    while Q:
        now=Q.popleft()
        if visited[now]:
            continue
        visited[now]=1
        for to in graph[now]:
            Q.append(to)
for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    for _ in range(E):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    