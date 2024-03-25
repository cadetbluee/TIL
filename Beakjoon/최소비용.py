import sys
input=sys.stdin.readline
#우선순위 큐를 활용
from heapq import heappush, heappop

def dijkstra(start,end):
    pq = []
    # weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)
        if visited[now]:
            continue
        visited[now]=1
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist  # 누적 거리를 최단 거리로 갱신
            
            heappush(pq, (new_dist, next_node))  # next_node의 인접 노드 pq에 추가

    
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    s,e,w=map(int,input().split())
    graph[s].append((w,e))
s,e=map(int,input().split())
distance=[1e9]*(N+1)
visited=[0]*(N+1)
dijkstra(s,e)
print(distance[e])