import sys
sys.stdin = open("5789_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N,Q=map(int,input().split())
    L=[]
    R=[]
    result=[0]*N
    for _ in range(Q):
        l,r=map(int,input().split())
        L.append(l)
        R.append(r)
    for i in range(1,Q+1):
        for j in range(L[i-1]-1,R[i-1]):
            result[j]=i
    print(f'#{test_case}',*result)