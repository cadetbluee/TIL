import sys
sys.stdin=open('5202_input.txt')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    truck=[]
    for _ in range(N):
        s,e=map(int,input().split())
        truck.append((s,e))
    truck.sort(key=lambda x:x[1])
    end_time=truck[0][1]
    cnt=1
    for i in range(1,N):
        if truck[i][0]>=end_time:
            cnt+=1
            end_time=truck[i][1]
    print(f'{tc} {cnt}')