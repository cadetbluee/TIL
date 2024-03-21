import sys
sys.stdin = open("5250_input.txt", "r")
from heapq import heappush, heappop
def dijkstra(start):
    pq = []
    # weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start[0]][start[1]] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)


        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        for to in graph[now[0]][now[1]]:
            next_dist = to[0]
            next_node = (to[1],to[2])

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node[0]][next_node[1]]:
                continue

            distance[next_node[0]][next_node[1]]= new_dist  # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_dist, next_node))  # next_node의 인접 노드 pq에 추가

T=int(input())
dirs=[(1,0),(0,1),(0,-1),(-1,0)]
for tc in range(1,T+1):
    N=int(input())
    graph = [[[]*N for _ in range(N)]for _ in range(N)]
    INF = int(1e9)
    distance = [[INF] * (N) for _ in range(N)]
    arr=[list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d in dirs:
                ni,nj=i+d[0],j+d[1]
                if 0<=ni<N and 0<=nj<N:
                    if arr[i][j]>=arr[ni][nj]:
                        w=1
                    else:
                        w=arr[ni][nj]-arr[i][j]+1
                    graph[i][j].append([w,ni,nj])
    start=(0,0)
    end=(N-1,N-1)
    # print(tc)
    # print(graph)
    dijkstra(start)

    print(f'#{tc} {distance[N-1][N-1]}')
