import sys
sys.stdin = open("1251_input.txt", "r")

from heapq import heappush, heappop
def prim(start):
    pq=[]
    MST=[0]*N
    #최소비용
    sum_weight=0

    #시작점 추가
    #[기존 BFS] 노드 번호만 관리
    #[PRIM] 가중치가 낮으면 먼저 나와야 한다
    # -> 관리해야 할 데이터: 가중치, 노드번호 2가지
    # -> 동시에 두 가지 데이터 다루기
    #       1. class로 만들기
    #       2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq,(0,start))
    while pq:
        weight,now=heappop(pq)
        #우선순위 큐의 특성상
        # 더 먼 거리로 가는 방법이 큐에 저장되어 있기 때문에
        #기존에 이미 더 짧은 거리로 방문했다면 continue
        if MST[now]:
            continue
        # 방문처리
        MST[now]=1
        #누적합 추가
        sum_weight+=weight

        #갈 수 있는 노드들을 보면서
        for to in range(N):
            #갈 수 없거나 이미 방문했다면 pass
            if graph[now][to]==0 or MST[to]:
                continue
            heappush(pq,(graph[now][to],to))
    sum_weight=round(sum_weight)
    print(f'#{tc} {sum_weight}')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr_x=list(map(int,input().split()))
    arr_y=list(map(int,input().split()))
    E=float(input())
    graph=[[0]*N for _ in range(N)]
    INF = int(1e9)
    distance = [[INF] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j !=i:
                graph[i][j]=round((((arr_x[i]-arr_x[j])**2+(arr_y[i]-arr_y[j])**2)**(1/2))**2*E,6)
    prim(0)