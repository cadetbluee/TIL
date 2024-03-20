#인접행렬 DFS : 재귀
graph=[
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
]

visited=[0]*5
path=[]
def dfs(now):
    # 기저조건
    # 지금 문제에선 없다

    # 다음 재귀함수 호출전 작업
    # visited[now]=1
    # path.append(now)
    #다음 재귀함수 호출
    #dfs:현재노드에서 다른 노드들을 확인
    #다른 노드들 ==반복문
    for to in range(5):
        #갈수없다면 pass
        if graph[now][to]==0:
            continue

        #이미 방문했다면 pass
        if visited[to]:
            continue
        #가기전에 작업 - 권장
        visited[to]=1
        path.append(to)
        dfs(to)
    #돌아왔을 때 작업
visited[0]=1
path.append(0) #출발점 작업을 해줘야 함
dfs(0)
print(path)