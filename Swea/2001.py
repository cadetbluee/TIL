import sys
sys.stdin = open("2001_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    array=[list(map(int,input().split())) for _ in range(N)]
    def dirs(M):
        result_list=[]
        for i in range(M):
            for j in range(M):
                result_list.extend([(i,j)])
        return result_list



    result = 0
    for i in range(N):
        for j in range(N):
            sum_m = 0
            for d in dirs(M):
                #print(d)
                ni = i + d[0]  # y방향
                nj = j + d[1]  # x방향
                if 0 <= ni < N and 0 <= nj < N:
                    sum_m+=array[ni][nj]
            if result<sum_m:
                result=sum_m
    # max_sum=0
    # for i in range(N):
    #     for j in range(N):
    #         for n in range(M):
    #             for m in range(M):
    #                 sum_m=0
    #                 if i+M<N and j+M<N:
    #                     sum_m+=array[i+n][j+m]
    #                 elif
    #                 if max_sum<sum_m:
    #                     max_sum=sum_m
    print(f'#{test_case} {result}')
