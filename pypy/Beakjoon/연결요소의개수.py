import sys
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
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
cnt=1
while 0 in visited[1:]:
    dfs(visited[1:].index(0)+1)
    cnt+=1
print(cnt)