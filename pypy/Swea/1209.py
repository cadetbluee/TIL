import sys
sys.stdin = open("sum_input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    test_num=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    max_arr=0
    for i in range(100):
        cnt=0
        for j in range(100):
            cnt+=arr[i][j]
        if cnt>max_arr:
            max_arr=cnt
    for j in range(100):
        cnt = 0
        for i in range(100):
            cnt += arr[i][j]
        if cnt > max_arr:
            max_arr = cnt
    cnt = 0
    for j in range(100):

        for i in range(100):
            if i==j:
                cnt += arr[i][j]
    if cnt > max_arr:
        max_arr = cnt
    cnt = 0
    for i in range(100):
        for j in range(99,-1,-1):
            if i+j==99:
                cnt += arr[i][j]
    if cnt > max_arr:
        max_arr = cnt
    print(f'#{test_num} {max_arr}')