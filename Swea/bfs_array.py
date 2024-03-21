# #인접행렬 BFS
# # 갈 수 있는 곳 다 가기
# # 방문순서대로 다음 노드 먼저 방문 -> 먼저 다음노드  FIFO -> queue(deque-이중연결리스트)
# graph=[
#     [0,1,0,1,0],
#     [1,0,1,0,1],
#     [0,1,0,0,0],
#     [1,0,0,0,1],
#     [0,1,0,1,0],
# ]
# def bfs(start):
#     visited=[0]*5
#     #시작노드를 큐에 추가
#     queue=[start]
#     visited[start]=1
#     while queue:
#         now=queue.pop(0)
#         print(now,end=' ')
#         #갈수있는 곳을 체크
#         for to in range(5):
#             if graph[now][to]==0:
#                 continue
#             if visited[to]:
#                 continue
#             visited[to]=1
#             queue.append(to)
# bfs(0)

from collections import defaultdict


def solution(tickets):
    answer = []
    dict_tree = defaultdict(list)
    for ticket in tickets:
        dict_tree[ticket[0]].append(ticket[1])
    visited=set()
    for k, v in dict_tree.items():
        dict_tree[k] = sorted(v,reverse=True)
    stack = []
    for ap in dict_tree['ICN']:
        stack.append(('ICN', ap))
    answer.append('ICN')
    while stack:
        depart,airport = stack.pop()
        if (depart, airport) in visited:
            continue
        answer.append(airport)
        visited.add((depart, airport))
        for ap in dict_tree[airport]:
            stack.append((airport,ap))
    print(dict_tree)
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))