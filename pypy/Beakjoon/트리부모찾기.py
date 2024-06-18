from collections import deque
N=int(input())
graph=[[] for _ in range(N+1)]
for _ in range (N-1):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
def bfs(start):
    Q=deque()
    Q.append((start,0))
    parent=[]
    while Q:
        now,p=Q.popleft()
        if visited[now]:
            continue
        parent.append((now,p))
        visited[now]=1
        for to in graph[now]:
            Q.append((to,now))
    return parent
visited=[0]*(N+1)
result=sorted(bfs(1),key=lambda x:x[0])
for i in result[1:]:
    print(i[1])