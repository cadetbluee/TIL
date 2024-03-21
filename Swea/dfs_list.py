#인접리스트 DFS : 재귀
graph=[
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
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

    #인접리스트
    # 차이점 1. 갈수없는 곳 조건 필요없음
    # 차이점 2. for 문 작성 수정
    for to in graph[now]:

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