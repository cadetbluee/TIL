from collections import deque
from heapq import heappop,heappush
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append((1,n2))
    graph[n2].append((1,n1))
# def bfs(start,target):
#     Q=deque()
#     Q.append((start,0))
#     while Q:
#         now,kevin=Q.popleft()
#         if visited[now]:
#             continue
#         if now==target:
#             return kevin
#         for to in graph[now]:
#             Q.append((to,kevin+1))

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


ans=[]
min_kevin=1e9

for i in range(1,1+N):
    sub_sum=0
    distance=[1e9]*(N+1)
    dijkstra(i)
    sub_sum=sum(distance[1:])
    min_kevin=min(min_kevin,sub_sum)
    ans.append((i,sub_sum))
result=1e9
for a in ans:
    if a[1]==min_kevin:
        result=min(a[0],result)
print(result)