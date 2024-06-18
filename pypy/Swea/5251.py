import sys

sys.stdin = open("5251_input.txt", "r")

from heapq import heappush, heappop
T=int(input().strip())
for tc in range(1,T+1):
    INF = int(1e9)

    V, E = map(int, input().split())
    start = 0  # 시작 노드 번호

    graph = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])


    def dijkstra(start):
        pq = []
        heappush(pq, (0, start))
        distance[start] = 0

        while pq:
            dist, now = heappop(pq)
            for to in graph[now]:
                next_dist = to[0]
                next_node = to[1]

                new_dist = dist + next_dist

                if new_dist >= distance[next_node]:
                    continue

                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))


    dijkstra(0)
    print(f'#{tc} {distance[-1]}')