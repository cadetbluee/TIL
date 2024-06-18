import sys
sys.stdin = open("6485_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N=int(input())
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=map(int,input().split())
    P=int(input())
    C=[0]*P
    result=[0]*P
    for i in range(P):
        C[i]=int(input())
    for i in range(P):
        cnt=0
        for j in range(N):
            if A[j]<=C[i]<=B[j] :
                cnt+=1

        result[i]=cnt
    print(f'#{test_case}',end=' ')
    for i in range(P):
        if i!=P-1:
            print(result[i],end=' ')
        else:
            print(result[i])