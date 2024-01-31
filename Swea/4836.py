import sys
sys.stdin = open("4836_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    squares=[list(map(int,input().split())) for _ in range(N)]
    blank_sq=[[0]*10 for _ in range(10)]

    for i in range(10):
        for j in range(10):
            for square in range(N):
                if squares[square][0]<=i<=squares[square][2] and squares[square][1]<=j<=squares[square][3]:
                    if blank_sq[i][j]==0:
                        blank_sq[i][j]=squares[square][4]
                    elif squares[square][4]!=blank_sq[i][j]:
                        blank_sq[i][j]=3
    cnt=0
    for i in range(10):
        for j in range(10):
            if blank_sq[i][j]==3:
                cnt+=1
    print(f'#{test_case} {cnt}')