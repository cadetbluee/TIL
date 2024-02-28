import sys
sys.stdin=open('5201_input.txt')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    weight=list(map(int,input().split()))
    truck=list(map(int,input().split()))
    weight.sort(reverse=True)
    truck.sort(reverse=True)
    ans=0
    p=0
    for i in range(M):
        for j in range(i+p,N):
            if truck[i]>=weight[j]:
                ans+=weight[j]
                break
            else:
                p+=1
    print(f'#{tc} {ans}')