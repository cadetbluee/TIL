N, M = map(int, input().split())
lst = list(range(1, N + 1))  # 1부터 N까지의 리스트 생성
for _ in range(M):
    i, j = map(int, input().split())
    lst[i - 1], lst[j - 1] = lst[j - 1], lst[i - 1]
print(*lst)