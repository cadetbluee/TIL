import sys
sys.stdin = open("4835_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        sum_n = 0
        for j in range(M):
            sum_n += num_list[i+j]
        sum_list.append(sum_n)

    print(f'#{test_case} {max(sum_list)-min(sum_list)}')
