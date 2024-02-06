import sys
sys.stdin=open("4865_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    str_n=input()
    str_m=input()
    max_cnt=0
    for i in str_n:
        cnt=0
        for j in str_m:
            if i==j:
                cnt+=1
        if cnt>max_cnt:
            max_cnt=cnt

    print(f'#{test_case} {max_cnt}')