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
                break
    for i in range(9):
        for j in range(9):
            cnt=0
            for k in range(9):
                if arr[j][i]==arr[k][i]:
                    cnt+=1
            if cnt>1:
                result=0
                break
    # for i in range(3):
    #     for j in range(3):
    #         cnt_l=[0]*10#검증용
    #         for m in range(3):
    #             for n in range(3):
    #                 cnt_l[arr[m+i*3][n+j*3]]+=1
    #         for x in cnt_l:
    #             if x!=1:
    #                result=0
    #                break
    for i in range(3):
        for j in range(3):
            cnt_x = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt_x[arr[3*i+k][3*j+l]] += 1

            for k in range(1, 10):
                if cnt_x[k] != 1:
                    result = 0
                    break

    print(f'{test_case} {result}')