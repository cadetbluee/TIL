import sys
sys.stdin = open("16910_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    i=0
    j=0
    cnt=0
    for i in range(1,N+1):
        for j in range(N+1):
            if i**2+j**2<=N**2:
                cnt+=1
    print(f'#{test_case} {cnt*4+1}')