import sys
sys.stdin = open("2001_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    array=[list(map(int,input().split())) for _ in range(N)]
    max_sum=0
    for i in range(N):
        for j in range(N):
            for n in range(M):
                for m in range(M):
                    sum_m=0
                    if i+M<N and j+M<N:
                        sum_m+=array[i+n][j+m]
                    elif
                    if max_sum<sum_m:
                        max_sum=sum_m
    print(f'#{test_case} {max_sum}')
