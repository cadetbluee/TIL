from heapq import heappop, heappush
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    ai,bi=map(int,input().split())
    graph[ai].append((1,bi))
    graph[bi].append((1,ai))
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
distance=[1e9]*(N+1)
dijkstra(1)
max_num=max(distance[1:])
a=distance.index(max_num)
print(a,max_num,distance.count(max_num))