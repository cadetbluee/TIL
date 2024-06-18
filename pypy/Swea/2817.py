import sys
sys.stdin=open('2817_input.txt')

T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    cnt=0
    for i in range(1<<N):
        sum_sub=0
        for j in range(N):
            if i & (1<<j):

                sum_sub+=arr[j]
        if sum_sub==K:
            cnt+=1
    print(f'#{tc} {cnt}')