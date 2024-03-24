import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[B].append(A)

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
max_com=0
result=[]
for i in range(1,N+1):
    visited=[0]*(N+1)
    bfs(i)
    a=sum(visited)
    max_com=max(max_com,a)
    result.append((i,a))
for r in result:
    if r[1]==max_com:
        print(r[0],end=' ')