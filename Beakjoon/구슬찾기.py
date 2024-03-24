def count_rows(who, won_lost, n):
    stack = [who]
    visited = [0] * (n+1)
    cnt = 0

    # 깊이 우선 탐색을 하며, 이긴/진 사람들을 리스트에 추가함
    # 추가할때마다 cnt + 1
    while stack:
        cur = stack.pop()
        if result_dict[cur][won_lost]:
            for next in result_dict[cur][won_lost]:
                if not visited[next]:
                    visited[next] = 1
                    stack.append(next)
                    cnt += 1
    # cnt를 반환
    return cnt


def solution(n, results):

    global result_dict
    
    # 딕셔너리 컴프리헨션으로 key i에 빈 리스트 2 개를 value로 저장 (나에게 진 선수들, 나를 이긴 선수들 저장)
    result_dict = {i: [[],[]] for i in range(n+1)}
    rank = [0] * (n+1)      # 순위가 확정된 경우 1, 확정되지 않은 경우 0
    for won, lost in results:   # won : 이긴 사람, lost : 진 사람
        result_dict[won][0].append(lost)    # 이긴 사람 key의 0번 요소에 진 사람을 append
        result_dict[lost][1].append(won)    # 진 사람 key의 1번 요소에 이긴 사람을 append

    for i in range(1, n+1): # 1 ~ n 순회
        if count_rows(i, 0, n)> n//2 or count_rows(i, 1, n) > n//2:    # 나보다 실력이 좋은 사람 + 안좋은 사람들의 합이 n-1이면
            rank[i] = 1

    answer = sum(rank)
    return answer

result_dict = {}

N,M=map(int,input().split())
graph=[]
for _ in range(M):
    a,b=map(int,input().split())
    graph.append([a,b])
print(solution(N,graph))