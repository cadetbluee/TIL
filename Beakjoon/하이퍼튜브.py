import sys
from heapq import heappush, heappop
input=sys.stdin.readline
def dijkstra(start):
    pq = []
    # weight, node 번호를 한 번에 저장
    heappush(pq, (1, start))
    # 시작 노드 초기화
    distance[start] = 1

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)
        print(dist,now)

        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        for to in graph[now]:
            next_dist = 1
            next_node = to

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist  # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_dist, next_node))  # next_node의 인접 노드 pq에 추가


        

N,K,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    arr=list(map(int,input().split()))
    for i in range(K):
        for j in range(K):
            if i!=j and arr[j] not in graph[arr[i]]:
                graph[arr[i]].append(arr[j])
start=(1,0)
visited=[0]*(N+1)
min_cnt=1e9
distance = [int(1e9)] * (N+1)
# while stack:
#     now,cnt=stack.pop()
#     if visited[now]==1:
#         continue
#     visited[now]=1
#     if now==N:
#         min_cnt=min(min_cnt,cnt)
#     for to in graph[now]:
#         stack.append((to,cnt+1))

dijkstra(1)
print(distance[N])