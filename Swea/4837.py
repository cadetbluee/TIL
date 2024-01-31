import sys
sys.stdin = open("4837_input.txt", "r")
import random
T = int(input())
arr = list(range(1, 13))

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # N = 찾을 부분집합 내 원소의 개수
    # K = 찾을 부분집합 내 원소의 합

    cnt = 0

    for i in range(1 << 12):
        arr_list = []
        for j in range(12):
            if i & (1 << j):
                arr_list.append(arr[j])
                #부분집합 리스트 만들기 끝
        if sum(arr_list) == K and len(arr_list) == N:
            cnt += 1
            #조건 판별

    print(f'#{test_case} {cnt}')