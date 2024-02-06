import sys
sys.stdin=open("1216_input.txt","r")

for tc in range(10):
    test_case = int(input())
    N=100
    arr = [input() for i in range(N)]
    max_cnt = 0
    for M in range(99,-1,-1):
        for i in range(N):
            for j in range(N-M):
                if arr[i][j] == arr[i][j + M - 1]:
                    for k in range(1, M):
                        if arr[i][j + k] != arr[i][j + M - 1 - k]:
                            break
                    else:
                        if max_cnt<M:
                            max_cnt=M

    for M in range(99, -1, -1):
        for i in range(N):
            for j in range(0, N - M ):
                if arr[j][i] == arr[j + M - 1][i]:
                    for k in range(1, M):
                        if arr[j + k][i] != arr[j + M - 1 - k][i]:
                            break
                    else:
                        if max_cnt < M:
                            max_cnt=M


    print(f'#{test_case} {max_cnt}')