def dfs(t, s, arr):
    global max_profit

    # 만약 현재 선택한 부분집합의 합이 C를 초과하면 이전까지의 최대 이익과 비교하여 갱신합니다.
    if len(s) > 0 and sum(s) > C:
        max_profit = max(max_profit, t - s[-1] ** 2)
        return

    # 현재 선택할 수 있는 원소들에 대해 탐색합니다.
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            dfs(t + arr[i] ** 2, s + [arr[i]], arr)
            visited[i] = False

import sys
import heapq

sys.stdin = open('2115_input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    # N: 농장의 크기, M: 선택할 수 있는 벌통의 수, C: 최대 용량
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 농장 정보를 입력받습니다.
    dirs = [(0, i) for i in range(M)]  # 이동할 수 있는 방향을 설정합니다.
    visited = [[0] * N for i in range(N)]  # 방문 여부를 체크하기 위한 배열입니다.
    profits = []  # 이익을 저장하기 위한 리스트입니다.

    # 모든 벌통의 위치에 대해 반복합니다.
    for k in range(N):
        for l in range(N - M + 1):
            max_profit = 0

            # 현재 위치부터 M개의 벌통을 선택하여 채집할 수 있는지 확인합니다.
            if sum(arr[k][l:l + M]) <= C:
                # 선택한 벌통들의 총 이익을 계산합니다.
                sub_sum = 0
                for i in arr[k][l:l + M]:
                    sub_sum += i ** 2
                max_profit = max(max_profit, sub_sum)
            else:
                visited = [0] * M  # 방문 여부를 초기화합니다.
                dfs(0, [], arr[k][l:l + M])  # DFS를 통해 최대 이익을 계산합니다.

            # 계산한 최대 이익을 우선순위 큐에 저장합니다.
            heapq.heappush(profits, (-max_profit, k, l))

    result = []
    while profits:
        mm, r, c = heapq.heappop(profits)

        # 이미 두 개의 최대 이익을 찾았으면 반복문을 종료합니다.
        if len(result) == 2:
            break

        # 이전에 이미 선택한 위치와 겹치는지 확인하고, 겹치는 경우 무시합니다.
        if len(result) == 1 and r == result[0][1] and abs(result[0][2] - c) <= M:
            continue

        result.append((-mm, r, c))  # 최대 이익을 결과 리스트에 추가합니다.

    # 결과를 출력합니다.
    print(f'#{tc}', result[0][0] + result[1][0])