import sys
sys.stdin = open("9367_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    list_n=list(map(int,input().split()))
    cnt=1
    max_cnt=1
    for i in range(N):
        if i !=N-1:
            if list_n[i]<=list_n[i+1]:
                cnt+=1
                if cnt>max_cnt:
                    max_cnt=cnt
            else:
                cnt=1
    print(f'#{test_case} {max_cnt}')