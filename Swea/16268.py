import sys
sys.stdin = open("16268_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(N)]
    dirs=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
    max_r=0
    for i in range(N):
        for j in range(M):
            #result = board[i][j]
            result=0
            for d in dirs:
                ni = i + d[0]  # y방향
                nj = j + d[1]  # x방향
                if 0 <= ni < N and 0 <= nj < M:
                    result+=board[ni][nj]
            if max_r<result:
                max_r=result

    print(f'#{test_case} {max_r}')