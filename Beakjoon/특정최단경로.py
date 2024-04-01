
from heapq import heappush, heappop

INF = int(200000000)

V, E = map(int, input().split())
start = 1  # 시작 노드 번호

# 인접 리스트
graph = [[] for _ in range(V+1)]
# 누적 거리 저장할 변수
distance = [INF] * (V+1)
# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

v1,v2=map(int,input().split())

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


dijkstra(start)
f=distance[v1]
f2=distance[v2]
distance = [INF] * (V+1)
dijkstra(v1)
s=distance[v2]
t2=distance[V]
distance = [INF] * (V+1)
dijkstra(v2)
t=distance[V]
s2=distance[v1]
INF = int(1e9)

if f+s+t>INF and f2+s2+t2>INF:
    print(-1)
else:
    print(min(f+s+t,f2+s2+t2))