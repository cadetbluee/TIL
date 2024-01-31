import sys
sys.stdin = open("1974_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr=[list(map(int,input().split())) for _ in range(9)]
    result=1
    for i in range(9):
        for j in range(9):
            cnt=0
            for k in range(9):
                if arr[i][j]==arr[i][k]:
                    cnt+=1
            if cnt>1:
                result=0
    for i in range(9):
        for j in range(9):
            cnt=0
            for k in range(9):
                if arr[j][i]==arr[k][i]:
                    cnt+=1
            if cnt>1:
                result=0
    N=0
    M=0
    for i in range(N,N+2):
        cnt=0
        for j in range(M,M+2):
            for k in range(M,M+2):
                if arr[i][j]==arr[i][k]:
                    cnt+=1
            if M==2 or M==5:
                M+=3
        if M==2 or M==5:
            N+=3
        if cnt>1:
            result=0

    print(f'{test_case} {result}')