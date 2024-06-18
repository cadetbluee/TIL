N=int(input())
graph=[[] for _ in range(N+1)]
while True:
    a,b=map(int,input().split())
    if a<0:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    Q=[(start,0)]
    while Q:
        now,rank=Q.pop(0)
        if visited[now]:
            continue
        visited[now]=1
        if 0 not in visited[1:]:
            return rank
        for to in graph[now]:
            Q.append((to,rank+1))
candidates=[]
min_rank=N
for i in range(1,N+1):
    visited=[0]*(N+1)
    temp=bfs(i)
    min_rank=min(min_rank,temp)
    candidates.append((i,temp))
president_candidates=[]
for candidate in candidates:
    if candidate[1]==min_rank:
        president_candidates.append(candidate[0])
print(min_rank,len(president_candidates))
print(*president_candidates)