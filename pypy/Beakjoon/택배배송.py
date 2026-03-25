import sys
sys.stdin=open('5972_input.txt')

import heapq
N,M=map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C=map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))
    
dist=[10**15]*(N+1)
dist[1]=0
pq=[]
heapq.heappush(pq,(0,1))
# cost를 앞에 적어서 소가 더 적은 곳으로 유인
while pq:
    cost,now=heapq.heappop(pq)
  
    if dist[now]<cost:
        continue
    for next,w in graph[now]:
        new_cost=cost+w
        if new_cost<dist[next]:
            dist[next]=new_cost
            heapq.heappush(pq,(new_cost,next))
print(dist[N])