import sys
sys.stdin = open("19661_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr=list(map(int,input().split()))
    cnt=0
    for i in range(1,1<<len(arr)):
        sub_sum = 0
        for j in range(len(arr)):
            #print(i)
            if i & (1 << j):  # i가 1인 경우만 출력
                sub_sum += arr[j]
        if sub_sum==0:
            cnt+=1
    print(cnt)