import sys
sys.stdin=open('1795_input.txt')
from heapq import heappush, heappop
from copy import deepcopy

INF = int(1e9)
def dijkstra(start):
    pq = []
    # weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)


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

T=int(input())
for tc in range(1,T+1):
    N,M,X=map(int,input().split())
    graph=[[] for i in range(N+1)]
    distance = [INF] * (N+1)
    for _ in range(M):
        x,y,c=map(int,input().split())
        graph[x].append([c,y])
    dijkstra(X)
    temp=deepcopy(distance)
    max_dist=0
    distance = [INF] * (N + 1)
    for i in range(1,N+1):
        dijkstra(i)
        max_dist=max(max_dist,temp[i]+distance[X])
        distance = [INF] * (N + 1)
    print(f'#{tc} {max_dist}')