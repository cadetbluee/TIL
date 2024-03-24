N=int(input())
m=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(m):
    ai,bi=map(int,input().split())
    graph[ai].append(bi)
    graph[bi].append(ai)
visited=[0]*(N+1)
def bfs(start):
    stack=[(start,0)]
    while stack:
        now,f=stack.pop(0)
        if f>2:
            continue
        if visited[now]:
            continue
        visited[now]=1
        for to in graph[now]:
            stack.append((to,f+1))
bfs(1)

print(visited.count(1)-1)