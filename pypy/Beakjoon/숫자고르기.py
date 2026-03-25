import sys
sys.stdin=open('2668_input.txt')

input = sys.stdin.readline

N = int(input())

# nums[i] = i가 가리키는 다음 숫자
nums = [0] + [int(input()) for _ in range(N)]

# 정답을 저장할 리스트
answer = []


def dfs(start, current, visited):
    """
    start: 처음 시작한 노드 (사이클 체크 기준)
    current: 현재 탐색 중인 노드
    visited: 현재 경로에서 방문한 노드 집합
    """

    # 현재 노드를 방문 처리
    visited.add(current)

    # 다음으로 이동할 노드
    next_node = nums[current]

    # ⭐ 핵심: 다시 시작점으로 돌아오면 사이클 완성
    if next_node == start:
        return True

    # 아직 방문하지 않은 노드라면 계속 탐색
    if next_node not in visited:
        if dfs(start, next_node, visited):
            return True

    # 사이클 못 찾은 경우
    return False


# 모든 숫자에 대해 시작점으로 시도
for i in range(1, N + 1):
    visited = set()  # ⭐ 매번 새로 초기화 (중요)

    # i에서 시작해서 사이클 만들 수 있으면 정답에 추가
    if dfs(i, i, visited):
        answer.append(i)


# 출력 형식 맞추기
answer.sort()
print(len(answer))
for x in answer:
    print(x)